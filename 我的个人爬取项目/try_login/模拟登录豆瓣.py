import requests
# 直接复制整个请求头 ，用Cookie模拟登录成功

class DBSpider:
    def __init__(self):
        self.post_url = 'https://accounts.douban.com/j/mobile/login/basic'
        self.url = 'https://www.douban.com/people/shpk74123/'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'bid=Lv8Qd36QXPU; __yadk_uid=eRxjcuIanuZ5tUH7Xz5jAUCItn8zF6pJ; ll="118172"; _vwo_uuid_v2=D9C0533142C07295DC3DA18BD59371CFD|2e18d7d251648e4dc78cc50ef5e7cfd4; ct=y; __utmc=30149280; push_noty_num=0; push_doumail_num=0; __utmv=30149280.20427; douban-fav-remind=1; douban-profile-remind=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1569288730%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DkVTeO2euHzasHvIpPwP_S_jCIEMTmBskOGbaru2JyTx6FRDiuEoVjZ7tFS0Hthiz%26wd%3D%26eqid%3Db2601653004af850000000045d89720a%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1883654966.1568973295.1569207710.1569288731.6; __utmz=30149280.1569288731.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="204270440:4FwFrk6O9iw"; ck=UwDa; ap_v=0,6.0; _pk_id.100001.8cb4=8f0d5ecf350456ac.1568973295.5.1569288758.1569208525.; __utmb=30149280.5.10.1569288731',
            'Host': 'www.douban.com',
            'Referer': 'https://www.douban.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        }

        self.session = requests.session()


    def get_html(self):
        data = {
            'name': '13067906601',
            'password': 'shpk74123',
            'remember': 'false'
        }
        # self.session.post(url=self.post_url,data=data)
        html = requests.get(url=self.url,headers=self.headers).text
        print(html)



    def run(self):
        self.get_html()

if __name__ == '__main__':
    spider = DBSpider()
    spider.run()



