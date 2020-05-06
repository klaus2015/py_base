import requests
"""
登录成功 session.post() + session.get()
"""
class DBSpider:
    def __init__(self):
        self.post_url = 'https://accounts.douban.com/j/mobile/login/basic'
        self.url = 'https://www.douban.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
        }

        self.session = requests.session()


    def get_html(self):
        data = {
            'name': '13067906601',
            'password': 'shpk74123',
            'remember': 'false'
        }
        self.session.post(url=self.post_url,data=data)
        html = self.session.get(url=self.url,headers=self.headers).text

        print(html)



    def run(self):
        self.get_html()

if __name__ == '__main__':
    spider = DBSpider()
    spider.run()
