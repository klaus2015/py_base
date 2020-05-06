import requests
from lxml import etree

word = input('请输入要翻译的单词：')
post_url = 'http://m.youdao.com/translate'
data = {
    'inputtext':word,
    'type':'AUTO'
}
html = requests.post(url=post_url,data=data).text
parse_html = etree.HTML(html)
re = parse_html.xpath('//ul[@id="translateResult"]/li/text()')[0]
print('结果：',re)

# def get_cookies():
#     cookie_str = "OUTFOX_SEARCH_USER_ID=-1258737612@10.169.0.83; JSESSIONID=aaaRPbU9VTB3V-mO4HJ0w; " \
#                  "OUTFOX_SEARCH_USER_ID_NCOO=1111840937.5782938; ___rl__test__cookies=1568264679590"
#     cookies = {}
#     for kv in cookie_str.split('; '):
#         cookies[kv.split('=')[0]] = kv.split('=')[1]
#     return cookies
#
# print(get_cookies())