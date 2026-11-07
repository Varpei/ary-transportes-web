#!/usr/bin/env python3
"""Processador determinístico do kit oficial de design e da foto do Sr. Ary."""
import unicodedata
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "src" / "assets" / "img" / "raw"
OPT_DIR = ROOT / "src" / "assets" / "img" / "optimized"


def norm(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII").lower()


def find_raw_file(include_words, exclude_words=None):
    exclude_words = exclude_words or []
    if not RAW_DIR.exists():
        return None
    for file_path in RAW_DIR.iterdir():
        stem = norm(file_path.stem)
        if file_path.is_file() and all(norm(word) in stem for word in include_words):
            if not any(norm(word) in stem for word in exclude_words):
                return file_path
    return None


def black_bg_to_transparent(image: Image.Image, threshold: int = 24) -> Image.Image:
    rgba = image.convert("RGBA")
    output = []
    for red, green, blue, _ in rgba.getdata():
        maximum = max(red, green, blue)
        if maximum <= threshold:
            output.append((0, 0, 0, 0))
        elif maximum < threshold + 28:
            alpha = int(((maximum - threshold) / 28.0) * 255)
            output.append((red, green, blue, alpha))
        else:
            output.append((red, green, blue, 255))
    rgba.putdata(output)
    bounds = rgba.getbbox()
    return rgba.crop(bounds) if bounds else rgba


def white_bg_to_silver_transparent(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    output = []
    for red, green, blue, _ in rgba.getdata():
        if red > 235 and green > 235 and blue > 235:
            output.append((0, 0, 0, 0))
        else:
            luminance = int(0.299 * red + 0.587 * green + 0.114 * blue)
            silver = min(255, max(165, 255 - int(luminance * 0.45)))
            output.append((silver, silver, min(255, silver + 8), 255))
    rgba.putdata(output)
    bounds = rgba.getbbox()
    return rgba.crop(bounds) if bounds else rgba


def crop_whatsapp_badge(image: Image.Image) -> Image.Image:
    width, height = image.size
    center_x, center_y = width // 2, int(height * 0.415)
    radius = int(min(width, height) * 0.255)
    box = (
        max(0, center_x - radius), max(0, center_y - radius),
        min(width, center_x + radius), min(height, center_y + radius),
    )
    cropped = image.crop(box).convert("RGBA").resize((160, 160), Image.Resampling.LANCZOS)
    mask = Image.new("L", (160, 160), 0)
    ImageDraw.Draw(mask).ellipse((2, 2, 158, 158), fill=255)
    cropped.putalpha(mask)
    return cropped


def save_from(source, output_name, transform, **save_options):
    if source:
        with Image.open(source) as image:
            transform(image).save(OPT_DIR / output_name, "WEBP", **save_options)
        print(f"[OK] {source.name} -> {output_name}")
        return True
    return False


def main():
    OPT_DIR.mkdir(parents=True, exist_ok=True)
    color_logo = OPT_DIR / "logo-ary-color.webp"

    silver_source = find_raw_file(["logo", "preto", "cinza"], ["cinza_preto"])
    if not save_from(silver_source, "logo-ary-silver.webp", black_bg_to_transparent, quality=92, lossless=True) and color_logo.exists():
        save_from(color_logo, "logo-ary-silver.webp", white_bg_to_silver_transparent, quality=92, lossless=True)
    silver = OPT_DIR / "logo-ary-silver.webp"
    if not save_from(find_raw_file(["logo", "cinza", "preto"], ["preto_cinza"]), "logo-ary-graphite.webp", lambda image: black_bg_to_transparent(image, 16), quality=90, lossless=True) and silver.exists():
        save_from(silver, "logo-ary-graphite.webp", lambda image: image, quality=90)
    if not save_from(find_raw_file(["logo", "verde", "azul"]), "logo-ary-dark-bg.webp", black_bg_to_transparent, quality=92, lossless=True) and color_logo.exists():
        save_from(color_logo, "logo-ary-dark-bg.webp", lambda image: image.convert("RGBA"), quality=90)
    if not save_from(find_raw_file(["roda", "van"], ["contato"]), "bg-rodape-van.webp", lambda image: image.convert("RGB"), quality=88):
        save_from(OPT_DIR / "banner-contatos-ary.webp", "bg-rodape-van.webp", lambda image: image.convert("RGB"), quality=85)
    save_from(find_raw_file(["roda", "contato"]), "rodape-van-contatos.webp", lambda image: image.convert("RGB"), quality=88)
    save_from(find_raw_file(["design", "exemplo"]), "guia-design-referencia.webp", lambda image: image.convert("RGB"), quality=85)
    save_from(find_raw_file(["logo", "whatsapp"]), "icon-whatsapp-ary.webp", crop_whatsapp_badge, quality=92, lossless=True)

    ary_source = find_raw_file(["homenagem"]) or find_raw_file(["seu", "ary"])
    if ary_source:
        def enhance(image):
            result = ImageEnhance.Contrast(ImageEnhance.Sharpness(image.convert("RGB")).enhance(1.15)).enhance(1.05)
            if result.width > 1200:
                ratio = 1200 / float(result.width)
                result = result.resize((1200, int(result.height * ratio)), Image.Resampling.LANCZOS)
            return result
        save_from(ary_source, "fundador-sr-ary.webp", enhance, quality=88)
    elif not (OPT_DIR / "fundador-sr-ary.webp").exists():
        save_from(OPT_DIR / "fiat-ducato-ext.webp", "fundador-sr-ary.webp", lambda image: image.convert("RGB"), quality=85)


if __name__ == "__main__":
    main()
