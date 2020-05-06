import requests
class DouBanLogin(object):
    def __init__(self):
        self.url = "https://accounts.douban.com/j/mobile/login/basic"
        self.headers = {
            "Origin": "https://accounts.douban.com",
            "Referer": "https://accounts.douban.com/passport/login_popup?login_source=anony",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        }
        self.data = {
            "ck": "",
            "name": "13067906601",
            "password": "shpk74123",
            "remember": "false",
            "ticket": "",
        }
        self.session = requests.session()

    def get_cookie(self):
        html = self.session.post(self.url,headers=self.headers,data=self.data).json()
        if html["status"] == "success":
            print("恭喜你，登陆成功")

    def get_user_data(self):
        url = 'https://www.douban.com/'
        html = self.session.get(url).text
        print(html)

    def run(self):
        """运行程序"""
        self.get_cookie()
        self.get_user_data()

if __name__ == '__main__':

    login = DouBanLogin()
    login.run()