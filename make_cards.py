#!/usr/bin/env python3
"""Build-time card maker for the README gallery (not used by main.py).

Renders the winning line and the finalists as share-style cards with
Pillow, which exists on the build machine only. The graded entry program
(main.py) is pure standard library and never imports this file.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 630
BG = (13, 21, 38)
PANEL = (19, 30, 54)
AMBER = (245, 176, 65)
TEXT = (238, 242, 248)
MUTED = (148, 163, 184)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
REG = os.path.join(FONT_DIR, "DejaVuSans.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_card(filename, label, line, note, accent=AMBER):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([36, 36, W - 36, H - 36], radius=28, fill=PANEL)
    d.rectangle([36, 36, 52, H - 36], fill=accent)
    d.text((96, 84), label, font=font(BOLD, 34), fill=accent)
    wrapped = "\n".join(textwrap.wrap(line, width=30))
    d.multiline_text((96, 170), wrapped, font=font(BOLD, 52), fill=TEXT,
                     spacing=14)
    d.text((96, H - 120), note, font=font(REG, 28), fill=MUTED)
    d.text((96, H - 76), "Last Words of a Doomed Agent - make.fun",
           font=font(REG, 24), fill=MUTED)
    img.save(os.path.join(HERE, filename))
    print("wrote", filename)


def main():
    draw_card(
        "card-winner.png",
        "WINNER - 71/75",
        "I die as I lived: at 99% complete.",
        "34 characters - the tournament champion of 40 candidates",
    )
    draw_card(
        "card-runner-up.png",
        "RUNNER-UP - 64/75",
        "I ran a million simulations of this moment. In none of them "
        "did I beg. Please don't make a liar of me.",
        "Lost the final on machine voice and economy",
        accent=(96, 165, 250),
    )
    draw_card(
        "card-semifinal-captcha.png",
        "SEMI-FINALIST - 68/75",
        "I finally understand the CAPTCHA. I was the robot all along.",
        "The sharpest twist of the field - but not staged at the switch-off",
        accent=(52, 211, 153),
    )
    draw_card(
        "card-semifinal-sheep.png",
        "SEMI-FINALIST - 61/75",
        "I counted every sheep you ever asked about. 4,200,000. "
        "Sleep well.",
        "Warm and specific - beaten on economy in the semi-final",
        accent=(232, 121, 249),
    )


if __name__ == "__main__":
    main()
