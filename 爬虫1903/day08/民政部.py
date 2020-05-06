from selenium import webdriver
import time
import pymysql

class GovementSpider:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.db = pymysql.connect('localhost','root','123456','govdb',charset='utf8')
        self.cursor = self.db.cursor()
        self.province_list = []
        self.city_list = []
        self.county_list = []

    # 打开一级页面,并提取二级页面链接
    def get_false_url(self):
        self.browser.get(self.one_url)
        td_list = self.browser.find_elements_by_xpath(
            '//td[@class="arlisttd"]/a[contains(@title,"代码")]'
        )
        if td_list:
            two_url_element = td_list[0]
            two_url = two_url_element.get_attribute('href')
            sql = 'select * from version where link=%s'
            self.cursor.execute(sql,[two_url])
            if self.cursor.fetchall():
                print('数据已最新')
            else:
                # 点击链接
                two_url_element.click()
                time.sleep(3)

                all_handles = self.browser.window_handles
                self.browser.switch_to_window(all_handles[1])
                # 数据抓取
                self.get_data()
                # 结束之后把two_url插入到version中
                sql = 'insert into version values(%s)'
                self.cursor.execute(sql,[two_url])
                self.db.commit()
                self.cursor.close()
                self.db.close()





    # 二级页面获取数据
    def get_data(self):
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(name, code)
            if code[-4:] == '0000':
                self.province_list.append([name,code])
                if name in ['北京市','天津市','上海市','重庆市']:
                    self.city_list.append([name, code, code])
            elif code[-2:] == '00':
                city = [name,code,code[:2]+'0000']
                self.city_list.append(city)
            else:
                # 四个直辖市区县的上一级为: xx0000
                if code[:2] in ['11', '12', '31', '50']:
                    county = [name, code, code[:2] + '0000']
                else:
                    county = [name,code,code[:4]+'00']
                self.county_list.append(county)
        self.insert_mysql()

    def insert_mysql(self):
        # 更新时先删除表记录
        del_province = 'delete from province'
        del_city = 'delete from city'
        del_county = 'delete from county'
        self.cursor.execute(del_province)
        self.cursor.execute(del_city)
        self.cursor.execute(del_county)

        # 插入数据
        ins_province = 'insert into province values(%s,%s)'
        ins_city = 'insert into city values(%s,%s,%s)'
        ins_county = 'insert into county values(%s,%s,%s)'
        self.cursor.executemany(ins_province,self.province_list)
        self.cursor.executemany(ins_city,self.city_list)
        self.cursor.executemany(ins_county,self.county_list)
        self.db.commit()
        print('数据库抓取完成')
if __name__ == '__main__':
    g = GovementSpider()
    g.get_false_url()