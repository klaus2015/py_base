from selenium import webdriver
import time

class JDSpider:
    def __init__(self):
        self.url = 'https://www.jd.com/'
        self.browser = webdriver.Chrome()

    def get_html(self):
        so = '//*[@id="key"]'
        button = '//*[@id="search"]/div/div[2]/button'
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(so).send_keys('爬虫书')
        self.browser.find_element_by_xpath(button).click()
        time.sleep(4)

    def parse_html(self):
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            item = {}
            item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
            item['comment'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
            item['market'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()

            print(item)

    def main(self):
        self.get_html()
        while True:
            self.parse_html()
            if self.browser.page_source.find('pn-next disabled') == -1:
                # 不是最后1页,找到下一页按钮
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(3)
            else:
                break



if __name__ == '__main__':
    j = JDSpider()
    j.main()
