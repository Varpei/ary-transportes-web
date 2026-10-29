#!/usr/bin/env python3
"""Classificador visual determinístico das 14 fotos reais da ARY."""
from pathlib import Path
from PIL import Image, ImageChops, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "src" / "assets" / "img" / "raw"
OPT_DIR = ROOT / "src" / "assets" / "img" / "optimized"
MAP_PATH = ROOT / "docs" / "MAPA_FOTOS_VERIFICADO.md"


def metrics(path):
    with Image.open(path) as source:
        image = source.convert("RGB")
        original_size = image.size
        image.thumbnail((240, 240))
    pixels = list(image.getdata())
    width, height = image.size

    def ratio(predicate, crop=None):
        area = image.crop(crop) if crop else image
        values = list(area.getdata())
        return sum(1 for pixel in values if predicate(*pixel)) / max(1, len(values))

    average = tuple(sum(pixel[index] for pixel in pixels) / len(pixels) for index in range(3))
    return {
        "size": original_size,
        "ratio": original_size[0] / original_size[1],
        "white": ratio(lambda r, g, b: r > 240 and g > 240 and b > 240),
        "green": ratio(lambda r, g, b: g > r + 25 and g > b + 10),
        "blue": ratio(lambda r, g, b: b > r + 15 and b > g + 5),
        "dark": ratio(lambda r, g, b: (r + g + b) / 3 < 75),
        "warm": average[0] - average[2],
        "lower_red": ratio(
            lambda r, g, b: r > 150 and g < 70 and b < 70,
            (0, int(height * 0.67), width, height),
        ),
        "right_red": ratio(
            lambda r, g, b: r > 150 and g < 70 and b < 70,
            (int(width * 0.8), 0, width, height),
        ),
        "right_orange": ratio(
            lambda r, g, b: r > 120 and 50 < g < 170 and b < 90 and r > g + 25,
            (int(width * 0.5), 0, width, height),
        ),
        "top_brightness": sum(
            pixel[0] + pixel[1] + pixel[2]
            for pixel in image.crop((0, 0, width, int(height * 0.35))).getdata()
        ) / max(1, int(width * height * 0.35) * 3),
    }


def trim_white_borders(image, padding=24):
    background = Image.new(image.mode, image.size, (255, 255, 255))
    bbox = ImageChops.difference(image, background).getbbox()
    if not bbox:
        return image
    return image.crop((
        max(0, bbox[0] - padding), max(0, bbox[1] - padding),
        min(image.width, bbox[2] + padding), min(image.height, bbox[3] + padding),
    ))


def blur_regions(image, boxes):
    width, height = image.size
    for x1, y1, x2, y2 in boxes:
        box = (int(width * x1), int(height * y1),
               int(width * x2), int(height * y2))
        region = image.crop(box).filter(ImageFilter.GaussianBlur(radius=18))
        image.paste(region, box)
    return image


def classify(files):
    data = {path: metrics(path) for path in files}
    remaining = set(files)
    result = {}

    white = sorted(remaining, key=lambda path: data[path]["white"], reverse=True)
    color_logo = next(path for path in white if data[path]["white"] > .65 and
                      data[path]["green"] + data[path]["blue"] > .03)
    result[color_logo] = ("logo-ary-color.webp", "frota-01.webp", [], True)
    remaining.remove(color_logo)
    mono_logo = next(path for path in remaining if data[path]["white"] > .60 and
                     data[path]["green"] + data[path]["blue"] < .03)
    result[mono_logo] = ("logo-ary-mono.webp", "frota-10.webp", [], True)
    remaining.remove(mono_logo)

    banner = next(path for path in remaining if data[path]["ratio"] > 1.5 and
                  data[path]["blue"] > .5 and data[path]["green"] > .15)
    result[banner] = ("banner-contatos-ary.webp", "frota-09.webp", [], False)
    remaining.remove(banner)
    square = next(path for path in remaining if .90 <= data[path]["ratio"] <= 1.15)
    result[square] = ("corolla-executivo.webp", "frota-07.webp", [], False)
    remaining.remove(square)
    detail = next(path for path in remaining if 1 / data[path]["ratio"] > 1.55)
    result[detail] = ("corolla-detalhe-vip.webp", "frota-13.webp", [], False)
    remaining.remove(detail)

    airport = max(remaining, key=lambda path: data[path]["dark"])
    result[airport] = ("corolla-aeroporto-imp.webp", "frota-06.webp",
                       [(0.44, 0.52, 0.49, 0.56)], False)
    remaining.remove(airport)
    red_interior = sorted(remaining, key=lambda path: data[path]["lower_red"], reverse=True)[:2]
    panel = max(red_interior, key=lambda path: data[path]["top_brightness"])
    interior = red_interior[0] if red_interior[1] == panel else red_interior[1]
    result[panel] = ("iveco-daily-painel.webp", "frota-02.webp",
                     [(0.60, 0.58, 0.73, 0.66)], False)
    result[interior] = ("van-interior-poltronas.webp", "frota-05.webp", [], False)
    remaining -= set(red_interior)

    pipes = max(remaining, key=lambda path: data[path]["right_orange"])
    result[pipes] = ("sprinter-turismo-pousada.webp", "frota-14.webp", [], False)
    remaining.remove(pipes)
    sunset = max(remaining, key=lambda path: data[path]["right_red"])
    result[sunset] = ("fiat-ducato-sunset.webp", "frota-03.webp", [], False)
    remaining.remove(sunset)
    left_plate = min(remaining, key=lambda path: data[path]["blue"])
    result[left_plate] = ("fiat-ducato-ext.webp", "frota-04.webp",
                          [(0.0, 0.68, 0.10, 0.80)], False)
    remaining.remove(left_plate)
    right_plate = max(remaining, key=lambda path: data[path]["ratio"])
    result[right_plate] = ("iveco-daily-ext.webp", "frota-08.webp",
                           [(0.75, 0.73, 0.95, 0.84)], False)
    remaining.remove(right_plate)
    warm = max(remaining, key=lambda path: data[path]["warm"])
    result[warm] = ("iveco-daily-5estrelas.webp", "frota-12.webp", [], False)
    remaining.remove(warm)
    cold = remaining.pop()
    result[cold] = ("mercedes-sprinter-ext.webp", "frota-11.webp", [], False)
    return result, data


def process(result):
    lines = ["# Mapa de Fotos Verificado", "",
             "Classificação visual executada sobre os arquivos raw reais; regiões sensíveis receberam blur.",
             "", "| Arquivo raw | Slot principal | Extra | Dimensões | Proteção |",
             "|---|---|---|---:|---|"]
    for source, (primary, extra, boxes, is_logo) in sorted(result.items(), key=lambda item: item[0].name):
        with Image.open(source) as original:
            image = original.convert("RGB")
        if is_logo:
            image = trim_white_borders(image)
        image = blur_regions(image, boxes)
        max_width = 800 if is_logo else 1280
        if image.width > max_width:
            ratio = max_width / image.width
            image = image.resize((max_width, int(image.height * ratio)), Image.Resampling.LANCZOS)
        image.save(OPT_DIR / primary, "WEBP", quality=85, method=6)
        image.save(OPT_DIR / extra, "WEBP", quality=85, method=6)
        protection = "crop logo" if is_logo else ("blur LGPD" if boxes else "nenhuma")
        lines.append(f"| `{source.name}` | `{primary}` | `{extra}` | {image.width}x{image.height} | {protection} |")
    MAP_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    OPT_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(path for path in RAW_DIR.iterdir()
                   if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"})
    if len(files) != 14:
        raise RuntimeError(f"Esperadas 14 imagens raw; encontradas {len(files)}.")
    result, _ = classify(files)
    process(result)
    print(f"=== CLASSIFICACAO CONCLUIDA: {len(result)}/14 fotos ===")
    for source, (primary, extra, _, _) in sorted(result.items(), key=lambda item: item[0].name):
        print(f"[OK] {source.name} -> {primary}, {extra}")


if __name__ == "__main__":
    main()
