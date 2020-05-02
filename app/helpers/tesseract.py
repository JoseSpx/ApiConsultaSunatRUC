from io import BytesIO
import requests
from PIL import Image
import pytesseract as tess

from app import app

tess.pytesseract.tesseract_cmd = app.config['TESSERACT_ROUTE']


def read_text_from_image_sunat(url_image):
    response_image = requests.get(url_image)
    cookies = response_image.cookies
    img = Image.open(BytesIO(response_image.content))
    img_text = tess.image_to_string(img)
    return img_text, cookies


