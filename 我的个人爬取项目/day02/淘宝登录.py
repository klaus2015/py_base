import requests
from selenium import webdriver
browser = webdriver.Chrome()
url = 'http://www.taobao.com/'

browser.get(url)
browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]').click()
browser.find_element_by_xpath('//*[@id="J_Quick2Static"]').click()
browser.find_element_by_id('TPL_username_1').send_keys('烦躁的巨魔')
browser.find_element_by_id('TPL_password_1').send_keys('zxm5984')
