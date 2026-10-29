"""Processa imagens da frota e garante todos os slots visuais do protótipo."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "src" / "assets" / "img" / "raw"
OPTIMIZED = ROOT / "src" / "assets" / "img" / "optimized"
SLOTS = {
    "logo-ary-color.webp": "ARY Transportes e Viagens",
    "logo-ary-mono.webp": "ARY Transportes e Viagens",
    "iveco-daily-ext.webp": "Iveco Daily 50-180 - 5 Estrelas",
    "iveco-daily-painel.webp": "Painel Iveco Daily",
    "mercedes-sprinter-ext.webp": "Mercedes-Benz Sprinter Executiva",
    "fiat-ducato-ext.webp": "Fiat Ducato Minibus",
    "van-interior-poltronas.webp": "Interior Executivo VIP",
    "corolla-executivo.webp": "Toyota Corolla Executivo",
    "corolla-aeroporto-imp.webp": "Receptivo Aeroporto de Imperatriz",
}


def placeholder(path, title):
    try:
        from PIL import Image, ImageDraw, ImageFont
        image = Image.new("RGB", (1280, 720), "#1B4956")
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, 1280, 18), fill="#8CC63F")
        font = ImageFont.load_default()
        lines = [title, "ARY Transportes e Viagens"]
        for index, line in enumerate(lines):
            box = draw.textbbox((0, 0), line, font=font)
            draw.text(((1280 - (box[2] - box[0])) / 2, 330 + index * 28), line,
                      fill="#F8FAFC", font=font)
        image.save(path, "WEBP", quality=82)
    except ImportError:
        path.write_bytes(b"BM" + bytes(70))


def convert(source, target):
    try:
        from PIL import Image, ImageFilter
        with Image.open(source) as image:
            image.thumbnail((1280, 1280), Image.Resampling.LANCZOS)
            image = image.convert("RGB")
            width, height = image.size
            plate_box = (
                int(width * 0.35),
                int(height * 0.68),
                int(width * 0.65),
                int(height * 0.92),
            )
            region = image.crop(plate_box).filter(ImageFilter.GaussianBlur(radius=12))
            image.paste(region, plate_box)
            image.save(target, "WEBP", quality=82, method=6)
    except ImportError:
        shutil.copyfile(source, target)


def main():
    OPTIMIZED.mkdir(parents=True, exist_ok=True)
    raw_files = sorted(
        p for p in RAW.iterdir()
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    )
    processed = []
    for index, source in enumerate(raw_files[:14], 1):
        target = OPTIMIZED / f"frota-{index:02d}.webp"
        convert(source, target)
        processed.append(source)

    for slot, title in SLOTS.items():
        target = OPTIMIZED / slot
        if target.exists():
            continue
        match = next(
            (source for source in processed
             if re.search(re.escape(slot.split(".")[0].split("-")[0]), source.name, re.I)),
            None
        )
        if match:
            convert(match, target)
        elif processed:
            convert(processed[list(SLOTS).index(slot) % len(processed)], target)
        else:
            placeholder(target, title)
    print(f"{len(raw_files)} imagens raw verificadas; {len(SLOTS)} slots garantidos.")


if __name__ == "__main__":
    main()
