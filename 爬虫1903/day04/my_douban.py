import requests
import os
url = "http://code.tarena.com.cn/AIDCode/aid1903/12-spider/spider_day02.zip"
headers = {"User-Agent" : "'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',"}
auth = ('tarenacode','code_2013')

res = requests.get(url=url,headers=headers,auth=auth)
html = res.text
filename = url.split('/')[-1]
with open(filename,'wb') as f:
    f.write(html)