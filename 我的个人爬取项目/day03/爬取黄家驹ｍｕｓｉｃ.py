import requests
from lxml import etree

# def saveSound(url, song_name):
#
#     # print(response.content)
#     root = (
#         "/home/tarena/python投稿/音乐爬取/music/%s.mp3"
#         % song_name
#     )
#     with open(root, "wb") as f:
#         header = {
#             "Origin": "https://music.163.com",
#             "Referer": "https://music.163.com/",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
#         }
#         r = requests.get(url, headers=header)
#         f.write(r.content)


def getHTML(url):
    header = {
        "Origin": "https://music.163.com",
        "Referer": "https://music.163.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    }
    response = requests.get(url, headers=header)
    response.encoding = "utf-8"
    html = response.text
    tree = etree.HTML(html)
    url = tree.xpath('//ul[@class="f-hide"]/li/a/@href')
    song_name = tree.xpath('//ul[@class="f-hide"]/li/a/text()')
    print(url)
    print(song_name)
    for index, i in enumerate(url):
        every_url = i.split("=")[-1]
        song = song_name[index]
        base_url = "http://music.163.com/song/media/outer/url?id=%s" % every_url
        print(base_url)
        # print("第" + str(index + 1) + "数据保存成功")
        # saveSound(base_url, song)
        'https://music.163.com/#/song?id=346576'
https://m801.music.126.net/20190928103759/0e4d031c581bb754d4c86527e8fce22c/jdyyaac/060f/0453/555d/1ee5873bbf39b4917149b70cd028b47a.m4a
http://m10.music.126.net/20190928105445/c34f1aa370ce1076553b14421d06737e/ymusic/b1c4/b5de/74d0/9158ae4873e10b743790320db9ef9b29.mp3

getHTML("https://music.163.com/artist?id=11127")