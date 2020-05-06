import requests
from lxml import etree
import re
from Crypto.Cipher import AES
import os
from queue import Queue
from threading import Thread
class DNSpider:
    def __init__(self):
        self.url = 'http://tts.tmooc.cn/studentCenter/toMyttsPage'
        self.headers = {
            'Cookies': 'isCenterCookie=no; eBoxOpenAIDTN201903=true; tedu.local.language=zh-CN; __root_domain_v=.tmooc.cn; _qddaz=QD.tg7m4y.vf9qa2.k2c0a1mo; Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1572278181,1572362818,1572448164; TMOOC-SESSION=6BBD2ADD097D4339A37176AA0932A871; sessionid=6BBD2ADD097D4339A37176AA0932A871|E_bfun09g; _qddab=3-fv3a24.k2g39maq; Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1572657760; cloudAuthorityCookie=0; versionListCookie=AIDTN201903; defaultVersionCookie=AIDTN201903; versionAndNamesListCookie=AIDTN201903N22NPython%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD%25E5%2585%25A8%25E6%2597%25A5%25E5%2588%25B6%25E8%25AF%25BE%25E7%25A8%258BV06N22N687128; courseCookie=AID; stuClaIdCookie=687128; Hm_lvt_e997f0189b675e95bb22e0f8e2b5fa74=1572368432,1572448508,1572535797,1572657804; Hm_lpvt_e997f0189b675e95bb22e0f8e2b5fa74=1572657804; JSESSIONID=0904C4D6E698C885C8864AA0EABCC286',
            "Host": "tts.tmooc.cn",
            "Referer": "http://tts.tmooc.cn/studentCenter/toMyttsPage",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        }
        self.headers1 = {
            "Origin": "http://tts.tmooc.cn",
            "Referer": "http://tts.tmooc.cn/video/showVideo?menuId=672192&version=AIDTN201903",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        }
        self.queue = Queue()

    def get_html(self,url):
        html = requests.get(url=url,headers=self.headers).text
        return html

    def get_re_list(self, html, xpath_bds):
        parse_obj = etree.HTML(html)
        li_list = parse_obj.xpath(xpath_bds)
        return li_list

    def get_course_link(self):
        html = self.get_html(self.url)
        xpath_bds = '//div[@class="course-menu"]/ul/li'
        li_list = self.get_re_list(html, xpath_bds)
        course_link_list = []
        for li in li_list:
            link = li.xpath('.//li[@class="sp"]/a/@href')[0].strip()
            course_link_list.append(link)
            # 多线程入队列
            self.queue.put(link)
        # 取消单进程列表
        # return course_link_list

    def get_two_page(self):

        # course_link_list = self.get_course_link()
        # if course_link_list:
        #     old_url = 'http://videotts.it211.com.cn/'
        #
        #     for link in course_link_list:
        #         html = self.get_html(link)
        #         xpath_bds = '//div[@class="video-list"]/p/@id'
        #         am_pm_list = self.get_re_list(html,xpath_bds)
        #         print(am_pm_list)
        #         for item in am_pm_list:
        #             tem_link = item.split('_')[1].split('.')
        #             # pm = am_pm_list[1].split('_')[1].split('.')
        #             # 上午或者下午的视频链接
        #             full_url = old_url + tem_link[0] + '/' + tem_link[0] + '.' + tem_link[1]
        #             # pm_link = old_url + pm[0] + '/' + pm[0] + pm[1]
        #             # /home/tarena/sp/19050531/aid19050531am/
        #             dir = '/home/tarena/sp/{}/{}/'
        #             dir_am_pm = dir.format(tem_link[0][3:11],tem_link[0])
        #             if not os.path.exists(dir_am_pm):
        #                 os.makedirs(dir_am_pm)
        #             self.get_media_link(full_url,dir_am_pm)
        while True:
            if self.queue.empty():
                break
            link = self.queue.get()
            old_url = 'http://videotts.it211.com.cn/'
            # http://c.it211.com.cn/aid19050826am/aid19050826am.m3u8
            # http: // c.it211.com.cn / A_VIP_TSD_E_PYTHON - WITH - SELENIUM_DAY01_01 / A_VIP_TSD_E_PYTHON - WITH - SELENIUM_DAY01_01.m3u8
            html = self.get_html(link)
            xpath_bds = '//div[@class="video-list"]/p/@id'
            am_pm_list = self.get_re_list(html,xpath_bds)
            print(am_pm_list)
            for item in am_pm_list:
                tem_link = item.split('_')[1].split('.')
                # pm = am_pm_list[1].split('_')[1].split('.')
                # 上午或者下午的视频链接
                full_url = old_url + tem_link[0] + '/' + tem_link[0] + '.' + tem_link[1]
                # pm_link = old_url + pm[0] + '/' + pm[0] + pm[1]
                # /home/tarena/sp/19050531/aid19050531am/
                # dir = '/home/tarena/sp/{}/{}/'
                dir = 'E:\\dn\\'
                dir_am_pm = dir.format(tem_link[0][3:11],tem_link[0])
                if not os.path.exists(dir_am_pm):
                    os.makedirs(dir_am_pm)
                self.get_media_link(full_url,dir_am_pm)

    # 保存视频
    def get_media_link(self,full_url,dir_am_pm):
        html = requests.get(url=full_url,headers=self.headers1).text

        pattern = re.compile('URI="(.*?)"',re.S)
        if pattern.findall(html):
            key_link =  pattern.findall(html)[0]

            keys = requests.get(url=key_link,headers=self.headers1).content
            print(keys)
            # 秘钥
            cryptor = AES.new(keys,AES.MODE_CBC,keys)
            pattern1 = re.compile('\n(http://videotts.*?ts)\n',re.S)
            # [http://videotts.it211.com.cn/aid19050531am/aid19050531am-123.ts,..]
            ts_list = pattern1.findall(html)
            for ts in ts_list:
                num = ts.split('-')[-1].split('.')[0]
                if len(num) == 1:
                    num = '%s' % ('00') + num + '.ts'
                elif len(num) == 2:
                    num = '%s' % ('0') + num + '.ts'
                elif len(num) == 3:
                    num = num + '.ts'
                filename = dir_am_pm + num
                print(filename)
                # if not os.path.exists(filename):
                #     os.makedirs(filename)
                # 判断视频是否存在
                if not os.path.exists(filename):
                    html = requests.get(url=ts,headers=self.headers1).content
                    print(html)
                    with open(filename,'wb') as f:
                        f.write(cryptor.decrypt(html))
                        print('{}创建成功'.format(filename))
                else:#存在跳过此链接
                    continue
        else:
            pass

    def main(self):
        self.get_course_link()
        t_list = []
        for i in range(10):
            t = Thread(target=self.get_two_page)
            t_list.append(t)
            t.start()
        for t in t_list:
            t.join()


if __name__ == "__main__":
    d = DNSpider()
    d.main()




