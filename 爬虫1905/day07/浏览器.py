from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.find_element_by_id('kw').send_keys('赵丽颖')
browser.find_element_by_id('su').click()