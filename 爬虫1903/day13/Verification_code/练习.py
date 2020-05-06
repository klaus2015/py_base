import pytesseract

from PIL import Image

img = Image.open('yzm5.jpg')
result = pytesseract.image_to_string(img)
print(result)