from selenium import webdriver

from PIL import Image
from ydmapi import *

# 设置分辨率
options = webdriver.ChromeOptions()
options.add_argument('window-size=1900x3000')
browser = webdriver.Chrome()
# 获取首页截图,为了获取验证码图片
def get_screen_shot():

    browser.get('http://www.yundama.com/')
    browser.save_screenshot('index.png')

# 从首页截图中获取验证码图片
def get_caphe():
    # 定位验证码元素的位置(x,y)
    location = browser.find_element_by_xpath('//*[@id="verifyImg"]').location
    # 大小(宽度,高度)
    size = browser.find_element_by_xpath('//*[@id="verifyImg"]').size
    # 左上角x坐标
    left = location['x']
    # 左上角y坐标
    top = location['y']
    # 右下角x坐标
    right = left + size['width']
    # 右下角y坐标
    bottom = top + size['height']

    # 截取验证码图片, crop():对图片剪切,参数为元组,根据坐标
    img = Image.open('index.png').crop((left,top,right,bottom))
    img.save('verify.png')
    result = get_result('verify.png')
    return result

if __name__ == '__main__':
    get_screen_shot()
    re = get_caphe()
    print(re)