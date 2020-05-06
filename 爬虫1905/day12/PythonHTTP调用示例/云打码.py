from selenium import webdriver
from PIL import Image
from ydmapi import get_result

class AttackYdm:
    def __init__(self):
        self.url = 'http://www.yundama.com/'
        self.browser = webdriver.Chrome()
    # 获取首页截图
    def get_index(self):
        self.browser.get(self.url)
        self.browser.save_screenshot('index.png')
    # 截取验证码图片
    def get_caphe(self):
        xpath_bds = '//*[@id="verifyImg"]'
        # 定位节点 x, y坐标
        location = self.browser.find_element_by_xpath(xpath_bds).location
        # 获取宽度和高度
        size = self.browser.find_element_by_xpath(xpath_bds).size
        # 左上角x,y
        left = location['x']
        top = location['y']

        # 右下角x, y
        right = left + size['width']
        bottom = top + size['height']
        img = Image.open('index.png').crop((left,top,right,bottom))
        img.save('yzm.png')
        result = get_result('yzm.png')
        print(result)

if __name__ == '__main__':
    a = AttackYdm()
    a.get_index()
    a.get_caphe()
