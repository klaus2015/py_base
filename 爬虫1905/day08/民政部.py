from selenium import webdriver
import pymysql
class GovSpider:
    def __init__(self):
        self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        # 无界面模式
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        self.db = pymysql.connect('127.0.0.1','root','123456',database='govdb',port=3306,charset='utf8')
        self.cursor = self.db.cursor()
        self.province = []
        self.city = []
        self.county = []
    def get_html(self):
        self.browser.get(self.one_url)
        # 找第一个包含代码的td的节点
        td = self.browser.find_element_by_xpath('//td[@class="arlisttd"]/a[contains(@title,"代码")]')
        print(td)
        if td:
            # get_attribute('href') 获取到的时完整的url，不需要拼接，注意
            # http://www.mca.gov.cn/article/sj/xzqh/2019/201908/20190800019143.shtml
            # href="/article/sj/xzqh/2019/201908/20190800019144.shtml" 网页中数据
            two_url = td.get_attribute('href')
            print(two_url)
            sql = 'select * from version where link=%s'
            # result 是受影响的条数
            result = self.cursor.execute(sql,[two_url])

            if result:
                print('网站未更新，无需抓取')
            else:
                td.click()
                self.get_code()
                # 把href放入version中
                dele = 'delete from version'
                sql = 'insert into version values(%s)'
                self.cursor.execute(dele)
                self.cursor.execute(sql,[two_url])
                self.db.commit()

    def get_code(self):
        # 切换句柄
        all_handles = self.browser.window_handles
        self.browser.switch_to_window(all_handles[1])
        # 抓数据
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(name,code)
            if code[-4:] == '0000':
                self.province.append([name,code])
                if name in ['北京市',['天津市'],['上海市'],['重庆市']]:
                    self.city.append([name,code,code])

            elif code[-2:] == '00':
                self.city.append([name,code,code[:2]+'0000'])

            else:
                if code[:2] in ['11', '12', '31', '50']:
                    self.county.append([name, code, code[:2] + '0000'])
                else:
                    self.county.append([name,code,code[:4]+'00'])
        self.insert_mysql()

    def insert_mysql(self):
        # 先清空表
        del_province = 'delete from province'
        del_city = 'delete from city'
        del_county = 'delete from county'
        self.cursor.execute(del_province)
        self.cursor.execute(del_city)
        self.cursor.execute(del_county)
        # 再插入数据
        ins_province = 'insert into province values(%s,%s)'
        ins_city = 'insert into city values(%s,%s,%s)'
        ins_county = 'insert into county values(%s,%s,%s)'
        self.cursor.executemany(ins_province, self.province)
        self.cursor.executemany(ins_city, self.city)
        self.cursor.executemany(ins_county, self.county)
        self.db.commit()
        print('数据抓取完成,成功存入数据库')

    def main(self):
        self.get_html()
        # 所有数据处理完成后断开连接
        self.cursor.close()
        self.db.close()
        # 关闭浏览器
        self.browser.quit()




if __name__ == "__main__":
    g = GovSpider()
    g.main()