import requests
import json

class DoubanSpider:
    def __init__(self):
        self.baseurl = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start=00&limit' \
                       '={}'
        # 正则批量处理headers
        self.headers = {
            'Accept': '*/*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'll="118172"; bid=0HXM0s5u-j8; __yadk_uid=Bs1pPFqZ22hoNiHkak1G70yqycxAnlVJ; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1566779599%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dhv7R9eWymjz8GPRSpHhCF9KP1mn3Y1JRHEz0K83sTIujQp9cmcsmxtp-mMqZNnkC%26wd%3D%26eqid%3Df0eb0a3f0008c5cd000000045d6328c7%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1687715924.1566737865.1566737865.1566779599.2; __utmc=30149280; __utmz=30149280.1566779599.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.574978414.1566737865.1566737865.1566779599.2; __utmb=223695111.0.10.1566779599; __utmc=223695111; __utmz=223695111.1566779599.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt_t1=1; ap_v=0,6.0; _vwo_uuid_v2=DE3080183EF1B3B866C1A06283AB18958|c8edb5fb9d76ac8ba95021bf41058e88; __gads=ID=a4a4fd66b2a1b841:T=1566779659:S=ALNI_MZVoAjoB8RQWf3G4DssCy1XifWF9A; _pk_id.100001.4cf6=0fbbce22471d3631.1566737868.2.1566779680.1566737936.; __utmb=30149280.18.8.1566779679736; RT=',
            'Host': 'movie.douban.com',
            'Pragma': 'no-cache',
            'Referer': 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def get_film_info(self,url):
        html_json = requests.get(url=url,
                                 headers=self.headers
                                 ).json()
        for film in html_json:
            # 名称
            name = film['title']
            score = film['score']
            print(name,score)

    def main(self):
        # 定义字典 :所有类型和对应的type的值
        type_dict = {'剧情':'11','喜剧':'24','爱情':'13'}
        film_type = input('请输入电影类型:(剧情|喜剧|爱情)')
        ty = type_dict.get(film_type, 'a')
        if ty != 'a':
            limit = input('请输入电影数量: ')
            url = self.baseurl.format(ty,limit)
            self.get_film_info(url)
        else:
            print('类型不存在')

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.main()


