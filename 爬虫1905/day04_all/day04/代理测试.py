import requests

url = 'http://httpbin.org/get'
headers = {
    'User-Agent':'Mozilla/5.0'
}
params = {
    'kw':'周习明'
}
# 定义代理,在代理IP网站中查找免费代理IP
proxies = {
    'http':'114.230.69.17:9999',
    'https':'27.204.112.20:9999'
}
try:
    html = requests.get(url,proxies=proxies,params=params,headers=headers,timeout=8).text

    print('200')
except Exception as e:
    print(404)
"""
{
  "args": {
    "kw": "zxm"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Cache-Control": "max-age=0", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0"
  }, 
  "origin": "27.204.112.20, 27.204.112.20", 
  "url": "https://httpbin.org/get?kw=zxm"
}
"""
"""
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Cache-Control": "max-age=259200", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0"
  }, 
  "origin": "27.204.112.20, 27.204.112.20", 
  "url": "https://httpbin.org/get"
}
"""