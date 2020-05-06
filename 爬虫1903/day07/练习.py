from selenium import webdriver
import time

b_xpath = '//*[@id="search"]/div/div[2]/button'
i_xpath = '//*[@id="key"]'
li_xpath = '//*[@id="J_goodsList"]/ul/li'


class JdSpider:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'https://www.jd.com/'
        self.n = 0

    def get_page(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(i_xpath).send_keys('python爬虫书')
        self.browser.find_element_by_xpath(b_xpath).click()
        time.sleep(4)

    def parse_page(self):
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(4)
        li_list = self.browser.find_elements_by_xpath(li_xpath)
        for li in li_list:
            info = li.text.split('\n')
            if info[0].startswith('每满'):
                price = info[1]
                name = info[2]
                number = info[3]
                market = info[4]
            elif info[0] == '单件':
                price = info[3]
                name = info[4]
                number = info[5]
                market = info[6]
            elif info[0].startswith('￥') and info[1].startswith('￥'):
                price = info[0]
                name = info[2]
                number = info[3]
                market = info[4]
            else:
                price = info[0]
                name = info[1]
                number = info[2]
                market = info[3]

            print(price, number, market, name)
            self.n += 1
            print('*' * 50)

    def main(self):
        self.get_page()
        for i in range(2):
            self.parse_page()
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(3)
                print(self.n)
            else:
                break


if __name__ == '__main__':
    spider = JdSpider()
    spider.main()
