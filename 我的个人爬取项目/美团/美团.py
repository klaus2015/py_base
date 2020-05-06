import requests
import random
import time
from lxml import etree
import re
url = 'https://hz.meituan.com/meishi/b8886/'
headers = {
"Connection": "keep-alive",
"Cookie": "_lxsdk_cuid=16d5e18b129c8-00f51cb0fcdd69-15231708-1fa400-16d5e18b129c8; wm_order_channel=default; utm_source=; uuid=da8977437a524095b4aa.1571622504.1.0.0; ci=50; rvct=50; client-id=ccc932c3-66b0-404f-88d7-045952de4a94; _lxsdk=16d5e18b129c8-00f51cb0fcdd69-15231708-1fa400-16d5e18b129c8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _hc.v=2ff3f734-a16f-f050-f598-b6d6e443fee3.1571623414; __mta=212097323.1571622521199.1571622975423.1571639204113.3; lat=30.403934; lng=120.301243; _lxsdk_s=16ded3e1dce-0fb-bc6-816%7C%7C19",
"Host": "hz.meituan.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
}

html = requests.get(url,headers=headers).text
print(html)


