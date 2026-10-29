#!/usr/bin/env python3
"""Mapeia as fotos reais aos slots e aplica proteção visual de privacidade."""
from pathlib import Path
from PIL import Image, ImageChops, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "src" / "assets" / "img" / "raw"
OPT_DIR = ROOT / "src" / "assets" / "img" / "optimized"

EXACT_MAP = [
    ("logo-ary-color.webp", ["frota-01.webp"], [], True),
    ("iveco-daily-painel.webp", ["frota-02.webp"], [(0.60, 0.58, 0.73, 0.66)], False),
    ("fiat-ducato-sunset.webp", ["frota-03.webp"], [], False),
    ("fiat-ducato-ext.webp", ["frota-04.webp"], [(0.0, 0.69, 0.09, 0.79)], False),
    ("van-interior-poltronas.webp", ["frota-05.webp"], [], False),
    ("corolla-aeroporto-imp.webp", ["frota-06.webp"], [(0.44, 0.52, 0.49, 0.56)], False),
    ("corolla-executivo.webp", ["frota-07.webp"], [], False),
    ("iveco-daily-ext.webp", ["frota-08.webp"], [(0.76, 0.74, 0.94, 0.83)], False),
    ("banner-contatos-ary.webp", ["frota-09.webp"], [], False),
    ("logo-ary-mono.webp", ["frota-10.webp"], [], True),
    ("mercedes-sprinter-ext.webp", ["frota-11.webp"], [], False),
    ("iveco-daily-5estrelas.webp", ["frota-12.webp"], [], False),
    ("corolla-detalhe-vip.webp", ["frota-13.webp"], [], False),
    ("sprinter-turismo-pousada.webp", ["frota-14.webp"], [], False),
]


def trim_white_borders(img, padding=24):
    background = Image.new(img.mode, img.size, (255, 255, 255))
    bbox = ImageChops.difference(img, background).getbbox()
    if not bbox:
        return img
    return img.crop((
        max(0, bbox[0] - padding),
        max(0, bbox[1] - padding),
        min(img.width, bbox[2] + padding),
        min(img.height, bbox[3] + padding),
    ))


def apply_privacy_blur(img, boxes):
    width, height = img.size
    for rx1, ry1, rx2, ry2 in boxes:
        box = (int(width * rx1), int(height * ry1),
               int(width * rx2), int(height * ry2))
        if box[2] > box[0] and box[3] > box[1]:
            img.paste(img.crop(box).filter(ImageFilter.GaussianBlur(radius=18)), box)
    return img


def find_source(index, preferred_name, raw_files):
    exact = RAW_DIR / preferred_name
    if exact.exists():
        return exact
    if index < len(raw_files):
        return raw_files[index]
    return None


def main():
    OPT_DIR.mkdir(parents=True, exist_ok=True)
    raw_files = sorted(
        path for path in RAW_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    )
    processed = 0
    for index, (primary, extras, blur_boxes, is_logo) in enumerate(EXACT_MAP):
        source = find_source(index, primary.replace(".webp", ".jpeg"), raw_files)
        if source is None:
            print(f"[AVISO] Nenhum arquivo encontrado para {primary}")
            continue
        with Image.open(source) as original:
            image = original.convert("RGB")
        if is_logo:
            image = trim_white_borders(image)
        image = apply_privacy_blur(image, blur_boxes)
        max_width = 800 if is_logo else 1280
        if image.width > max_width:
            ratio = max_width / float(image.width)
            image = image.resize((max_width, int(image.height * ratio)), Image.Resampling.LANCZOS)
        image.save(OPT_DIR / primary, "WEBP", quality=85, method=6)
        for extra in extras:
            image.save(OPT_DIR / extra, "WEBP", quality=85, method=6)
        processed += 1
        print(f"[OK] {source.name} -> {primary} ({image.width}x{image.height})")
    print(f"=== MAPEAMENTO CONCLUIDO: {processed}/14 fotos reais vinculadas ===")


if __name__ == "__main__":
    main()
