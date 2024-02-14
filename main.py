import qrcode
import os
from PIL import Image, ImageDraw, ImageFont


def create_qr_image(data, title, root='.'):
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

    my_font = ImageFont.truetype('Dosis-Bold.ttf', 36)
    draw = ImageDraw.Draw(img)
    print(title)
    draw.text((img.width / 2, img.height - 22), title, fill='black', font=my_font, anchor='mm')
    img.save(f"{root}/{title}.png")


def bulk_create_qr_code(*data, labelling: callable = lambda x: f'{x}', root='.'):
    for d in data:
        create_qr_image(d, labelling(d), root)


if __name__ == '__main__':
    bulk_create_qr_code(1, 2, 3, labelling=lambda x: f'{x}^', root='.')
