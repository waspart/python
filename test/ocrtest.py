import pytesseract
from PIL import Image

image = Image.open('img.jpg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)