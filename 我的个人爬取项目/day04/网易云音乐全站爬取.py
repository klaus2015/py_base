from urllib import parse
import requests
from lxml import etree

class WYSpider:
    def __init__(self):
        self.playlist_url = 'https://music.163.com/discover/playlist'
        self.cat = 'https://music.163.com/discover/playlist/?cat={}'
        self.page_url = 'https://music.163.com/discover/playlist/?order=hot&cat={}&limit=35&offset={}'
        self.detial_url = 'https://music.163.com{}'
        self.headers = {
            "cookie": "_iuqxldmzr_=32; _ntes_nnid=caaa989c24e036fd5cb56374742ec1cc,1569308178737; _ntes_nuid=caaa989c24e036fd5cb56374742ec1cc; WM_TID=gcv%2Bi5bfmb5AVRQBBEIt4mlZEfw%2F%2FaKI; WM_NI=98IabASGl3RUurPMtE6anzEqhtlR9cg8XqwrvhCVtwUbNx2%2FuanMWDLQuPLWSWJKXa9zkYVbnnzxUnOlIbq3wCkfUxY5q2EUfuyWpU691czVS5QbZEcDyKukIUHik6Q%2BRDg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee88c85a89b384d1e15df28a8fa7c84f869a9bafb87cf1adac8cc9638697add8c42af0fea7c3b92afbe88782e14b9199a4d4d15fb7aea0aef74ff6bfa29bc87bacaca4b3bc69a5e89892f67ab6b88db7f77d97be8299b125b7bfa2aed650908fbbb1cf5d918986acdb6bfba6a5bad56aaeb2b699d8668db48783f439b59da587d8749bebbfd3c85fa6abb7b8f35ff6e7ff84f95e91eb9f83d94fa19cb7acf8618b8b888aea3e93f59ea5e637e2a3; playerid=40876690; JSESSIONID-WYYY=9j8Uhf3xsCGlqbTwRJtcRilCwYthHbNIUZ%5CJiesKumpfjacAdzaqKkF7sPbZE7wEnGQgacdx8kuCZQuP0vRVikS25iqmtEUd0EcW%2FQz5%5ChTTZZ6hF8RfDEkvIf4H%2BQvRyM4W%5CUYiaQVk%5CMSuDOW%2Bvy7RD%5CXiabDW%2Bszz7gYToI8fwz61%3A1569651323174",
            "referer": "https://music.163.com/",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        }
    
    def get_html(self,url):
        html = requests.get(url=url,headers=self.headers).text
        return html

    def get_result_list(self,html,xpathbds):
        parse_obj = etree.HTML(html)
        re_list = parse_obj.xpath(xpathbds)
        return re_list
    
    def get_cat_link(self):
        html = self.get_html(self.playlist_url)
        # print(html)
        xpathbds = '//dd/a/@data-cat'
        cat_list = self.get_result_list(html,xpathbds)
        print(cat_list[:5])
        for cat in cat_list[:5]:
            cat = parse.quote(cat)
            # cat_link = self.cat.format(cat)
            self.parse_one_page(cat)

    def parse_one_page(self,cat):
        # 拼出欧美第一页ｕｒｌ
        while True:
            offset = 0
            page_url = self.page_url.format(cat,offset)
            html = self.get_html(page_url)
            # print(html)
            xpathbds = '//a[@class="zbtn znxt js-disabled"]'
            btn_next = self.get_result_list(html,xpathbds)
            if not btn_next:
                # 不到最后一页，一直累加
                offset += 35
                print(offset)
            else:
                # 最后一页直接ｂｒｅａｋ此次循环
                break












if __name__ == "__main__":
    w = WYSpider()
    w.get_cat_link()





















