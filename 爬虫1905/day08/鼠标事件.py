from selenium import webdriver
from selenium.webdriver import ActionChains

# 打开浏览器 输入百度 + 找到设置节点

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
set_node = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
# 鼠标移动到 设置 节点
mouse_obj = ActionChains(browser)
mouse_obj.move_to_element(set_node)
mouse_obj.perform()

# 找高级搜索 节点， 并点击

browser.find_element_by_link_text('高级搜索').click()