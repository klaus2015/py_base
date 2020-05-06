import requests
url = 'https://m701.music.126.net/20190928105540/ce45488071fbbefb0cf94423eee68997/jdyyaac/060f/0453/555d/1ee5873bbf39b4917149b70cd028b47a.m4a'
from urllib import parse

s = parse.unquote(url)
print(s)
# 4个语种的url链接
url= 'https://music.163.com/discover/playlist'
#  dl[class="f-cb"][1]//a[class="s-fc1"]/@data-cat   ---欧美　日韩　粤语
# 欧美
url = 'https://music.163.com/discover/playlist/?cat=%E6%AC%A7%E7%BE%8E'
# 欧美第一页 two
url= 'https://music.163.com/discover/playlist/?order=hot&cat=%E6%AC%A7%E7%BE%8E&limit=35&offset=0'
url= 'https://music.163.com/discover/playlist/?order=hot&cat=%E6%AC%A7%E7%BE%8E&limit=35&offset=35'
url = 'https://music.163.com/discover/playlist/?order=hot&cat=%E6%97%A5%E8%AF%AD&limit=35&offset=70'

#　找到一页中所有详情页ｉｄ
# //p[@class="dec"]/a/@href     ['/playlist?id=2956865402','/playlist?id=2956865402']

# 第一页第一个详情链接
'https://music.163.com' + '/playlist?id=2829816518'
url = 'https://music.163.com/playlist?id=2829816518' # 拼接

# 下一页 class
# //a[class="zbtn znxt"]/text()
# zbtn znxt js-disabled
# //a[contains(@class,'js-disabled')]