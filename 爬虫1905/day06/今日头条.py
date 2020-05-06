import requests
from fake_useragent import UserAgent
from urllib.parse import urlencode
class JRSpider:
    def __init__(self):
        self.url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1568701619814'
        self.headers = {


            "cookie": "tt_webid=6737059507559826955; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6737059507559826955; csrftoken=6fc10d1e2879e9ee679bb204b190eba3; s_v_web_id=7ace41209cec0fd780905f8af8007ffb; __tasessionId=wx5nmajln1568706244889",
            "pragma": "no-cache",
            "referer": "https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }


    def get_html(self):
        response = requests.get(url=self.url,headers=self.headers)
        try:
            if response.status_code == 200:
                # 如果状态码为200（即响应成功）则返回json格式的响应内容
                # 在requests中自带json()方法
                return response.json()
            else:
                return None
        except Exception as f:
            return None

    def parse_html(self):
        html = self.get_html()
        for item in html['data']:
            title = item['title']
            print(title)

j = JRSpider()
j.parse_html()