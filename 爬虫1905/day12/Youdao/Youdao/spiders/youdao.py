# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import YoudaoItem
import time
import random
from hashlib import md5
class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    word = input("请输入要翻译的单词： ")
    def start_requests(self):
        post_url = 'http://fanyi.youdao.com/' \
                        'translate_o?smartresult=dict&' \
                        'smartresult=rule'

        ts, salt, sign = self.get_salt_sign_ts(self.word)
        formdata = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "a4f4c82afd8bdba188e568d101be3f53",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # cookies = self.get_cookies()
        # post请求: scrapy.FormRequest()
        # get请求:  scrapy.Request()
        yield scrapy.FormRequest(
            url=post_url,
            #cookies=cookies,
            formdata=formdata,
            callback=self.parse
        )

    # def get_cookies(self):
    #     cookie_str = "OUTFOX_SEARCH_USER_ID=-1258737612@10.169.0.83; JSESSIONID=aaaRPbU9VTB3V-mO4HJ0w; " \
    #                  "OUTFOX_SEARCH_USER_ID_NCOO=1111840937.5782938; ___rl__test__cookies=1568264679590"
    #     cookies = {}
    #     for kv in cookie_str.split('; '):
    #         cookies[kv.split('=')[0]] = kv.split('=')[1]
    #     return cookies


    def get_salt_sign_ts(self,word):
        # ts
        ts = str(int(time.time() * 1000))
        # salt
        salt = ts + str(random.randint(0, 9))
        # sign
        string = "fanyideskweb" + word + salt + \
                 "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    def parse(self, response):
        item = YoudaoItem()
        print(response.text)
        html = json.loads(response.text)
        item['result'] = html['translateResult'][0][0]['tgt']
        yield item
