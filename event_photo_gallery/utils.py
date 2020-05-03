from io import BytesIO
import string
import random
from PIL import Image, ExifTags
import piexif
from werkzeug.datastructures import FileStorage

def generate_passcode(size=12, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def rotate_jpeg(img):
    image = Image.open(img)
    if "exif" in image.info:
        exif_dict = piexif.load(image.info['exif'])

    
    result = BytesIO()
    if piexif.ImageIFD.Orientation in exif_dict['0th']:
        orientation = exif_dict['0th'][piexif.ImageIFD.Orientation]
        orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
        exif_bytes = piexif.dump(exif_dict)
        if orientation == 2:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            image = image.rotate(180)
        elif orientation == 4:
            image = image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 5:
            image = image.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 6:
            image = image.rotate(-90, expand=True)
        elif orientation == 7:
            image = image.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 8:
            image = image.rotate(90, expand=True)
        image.save(result, format="jpeg", exif=exif_bytes)
    else:
        image.save(result, format="jpeg")
    image.close()
    result.seek(0)
    img.stream = result
