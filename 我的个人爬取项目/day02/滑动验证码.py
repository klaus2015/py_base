from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

EMAIL = 'last@last.com'
PASSWORD = '123456'
class GG:
    def __init__(self):
        self.url = 'https://auth.geetest.com/login/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_greetests_button(self):
        button = self.browser.find_element_by_class_name('geetest_radar_tip')
        return button

