import qrcode
import os
from PIL import Image, ImageDraw, ImageFont


def create_qr_image(data, title, font_size, root='.'):
    if not os.path.isdir(root):
        raise NotADirectoryError('NotADirectoryError: Provided destination is not a directory')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make()
    img = qr.make_image()  # fill_color=(0, 255, 255), back_color=(255, 0, 255))

    img.save(f'{root}/{title}.png')
    img = Image.open(f'{root}/{title}.png')

    my_font = ImageFont.truetype('Dosis-Bold.ttf', font_size)
    draw = ImageDraw.Draw(img)
    draw.text((img.width / 2, img.height - 22), title, fill='black', font=my_font, anchor='mm')
    img.save(f"{root}/{title}.png")


if __name__ == '__main__':
    for i in range(1, 11):
        create_qr_image(i, f'{i}^', 36, root='./1^.png')
