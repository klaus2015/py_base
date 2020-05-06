import pytesseract
# Python图片处理标准库
from PIL import Image

# 创建图片对象
img = Image.open('p1.jpg')
img = img.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
img = img.point(table,'1')
img.show()
# 图片转字符串
result = pytesseract.image_to_string(img)
print(result)