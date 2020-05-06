s = """
#EXT-X-ALLOW-CACHE:YES
#EXT-X-TARGETDURATION:63
#EXT-X-KEY:METHOD=AES-128,URI="http://videotts.it211.com.cn/aid19050531am/static.key"
#EXT-X-ALLOW-CACHE:YES
#EXT-X-TARGETDURATION:63
#EXTINF:61.804000,

http://videotts.it211.com.cn/aid19050531am/aid19050531am-1.ts
#EXTINF:61.989000,
http://videotts.it211.com.cn/aid19050531am/aid19050531am-21.ts
#EXTINF:62.223000,
http://videotts.it211.com.cn/aid19050531am/aid19050531am-123.ts
#EXTINF:62.348000,

#EXTINF:62.380000,
"""
import re
pattern = re.compile('URI="(.*?)"',re.S)
re_list = pattern.findall(s)[0]
print(re_list)
# p1 = re.compile('\n(http://videotts.*?ts)\n',re.S)
# re_l = p1.findall(s)
# print(re_l)
# for item in re_l:
#
#     num = item.split('-')[-1].split('.')[0]
#     if len(num) == 1:
#         filename = '%s' % ('00') + num + '.ts'
#     elif len(num) == 2:
#         filename = '%s' % ('0') + num + '.ts'
#     elif len(num) == 3:
#         filename = num + '.ts'
#     print(filename)

'http://videotts.it211.com.cn/aid19050531am/aid19050531am.m3u8'
'http://videotts.it211.com.cn/aid19050531am/aid19050531amm3u8'
o = 'http://videotts.it211.com.cn/'
tt = 'active_aid19050531pm.m3u8'
'http://videotts.it211.com.cn/aid19050531am/aid19050531am.m3u8'
'http://videotts.it211.com.cn/aid19050531am/aid19050531am.m3u8'