import random
import time

import requests
import os
from requests import codes
from hashlib import md5
class JRSpider:
    def __init__(self):
        self.url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}' \
                   '&format=json&keyword=%E8%A1%97%E6%8B%8D'
        self.headers = {
            "cookie": "tt_webid=6737813695247713799; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6737813695247713799; csrftoken=8164c0053fa54354e61392cc8d201fdf; s_v_web_id=7be7cfc345aa8325491db2fe1da75e4d; __tasessionId=ml33ph96l1568793425708",
            "referer": "https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
        }
        self.i = 0

    def get_html(self,url):
        try:
            html = requests.get(url=url,headers=self.headers)
            if html.status_code == 200:

                return html.json()
        except Exception as e:
            return None

    def parse_html(self,url):
        html_json = self.get_html(url)
        if html_json.get('data'):
            for item in html_json.get('data'):
                if item.get('title') is None:
                    continue
                title = item.get('title')
                images = item.get('image_list')
                for image in images:
                    img_link = image.get('url')
                    item = {
                        'img_link':img_link,
                        'title':title
                    }
                    self.save_image(item)

    def save_image(self,item):
        img_path = 'img/' + item.get('title') + '/'
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        try:
            res = requests.get(item.get('img_link'))
            if codes.ok == res.status_code:
                file_path = img_path + '{}.{}'.format(
                    md5(res.content).hexdigest(),'jpg'
                )
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(res.content)
                    print('Downloaded image path is %s' % file_path)
                else:
                    print('Already Downloaded', file_path)
        except Exception as e:
            print(e)
    def main(self):
        for i in range(10):
            offset = i * 20
            url = self.url.format(offset)

            self.parse_html(url)

            time.sleep(random.randint(1,3))

if __name__ == "__main__":
    j = JRSpider()
    j.main()