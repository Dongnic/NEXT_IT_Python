import textwrap

from PIL import ImageFont, ImageDraw, Image


def make_image(msg):
    # image Size
    size = len(msg)
    fontS = 100
    W = 82 * size
    H = fontS + 20
    # 배경색
    bg_color = 'rgb(255, 255, 255)'
    # 글씨 설정
    font = ImageFont.truetype('../day15/BMYEONSUNG_ttf.ttf', size=100)
    font_color = 'rgb(255, 162, 255)'
    image = Image.new('RGB', (W, H), color=bg_color)
    draw = ImageDraw.Draw(image)
    lines = textwrap.wrap(msg, width=40)
    x_text = 10
    y_text = 10
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x_text, y_text), line, font=font, fill=font_color)
        y_text += height
    path='{}.png'.format(msg)
    image.save(path)
    return path

image_path = make_image('한산대첩')