from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://maoyan.com/board/4?offset=0')

# 基准xpath
li_list = browser.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
for li in li_list:
    item = {}
    info_list = li.text.split('\n')
    item['number'] = info_list[0]
    print(item)