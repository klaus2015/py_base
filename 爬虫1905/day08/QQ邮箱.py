from selenium import webdriver


url = 'https://mail.qq.com/'
browser = webdriver.Chrome()
browser.get(url)

# 切换到iframe框架 页面套页面
login_iframe = browser.find_element_by_id('login_frame')
browser.switch_to.frame(login_iframe)

# 找节点
user = browser.find_element_by_id('u').send_keys('598467866')
pwd = browser.find_element_by_id('p').send_keys('shpk74123')
browser.find_element_by_id('login_button').click()


