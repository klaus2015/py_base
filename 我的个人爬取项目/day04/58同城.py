import requests
import re
import time
import base64
from fontTools.ttLib import TTFont
from lxml import etree
class TCSpider:
    def __init__(self):
        self.url = 'https://su.58.com/qztech/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }


    def get_data(self):
        html = requests.get(url=self.url,headers=self.headers).text
        pattern = re.compile(r'@font-face.*?;base64,(.*?)\)', re.S)
        font_data_origin = pattern.findall(html)[0]
        font_data_after_decode = base64.b64decode(font_data_origin)

        new_font_name = "font_new.ttf"
        with open(new_font_name, 'wb') as f:
            f.write(font_data_after_decode)

        map_data = self.tff_parse(new_font_name)
        parse_obj = etree.HTML(html)
        names = parse_obj.xpath('//dd[@class="w70 stonefont resumeName"]/text()')
        if names:
            for name in names:
                print('name in page source', name)
                for j in map_data.keys():
                    name = name.replace(j, map_data[j])
                print('name actual', name)

    def tff_parse(self,font_parse_name):
        font_dict = [u'生', u'李', u'3', u'赵', u'专', u'吴', u'校', u'中', u'博', u'男', u'E', u'黄', u'7',
                     u'8', u'士', u'无', u'9', u'5', u'高', u'4', u'杨', u'A', u'经', u'验', u'张', u'硕',
                     u'下', u'1', u'B', u'女', u'周', u'王', u'0', u'M', u'技', u'6', u'应', u'大', u'2', u'陈',
                     u'本', u'科', u'刘', u'界',u'以']
        font_base = TTFont('font_base.ttf')
        font_base_order = font_base.getGlyphOrder()[2:]
        # font_base.saveXML('font_base.xml')  调试用

        font_parse = TTFont(font_parse_name)
        # font_parse.saveXML('font_parse_2.xml')调试用
        font_parse_order = font_parse.getGlyphOrder()[2:]

        f_base_flag = []
        for i in font_base_order:
            flags = font_base['glyf'][i].flags
            f_base_flag.append(list(flags))

        f_flag = []
        for i in font_parse_order:
            flags = font_parse['glyf'][i].flags
            f_flag.append(list(flags))

        result_dict = {}
        for a, i in enumerate(f_base_flag):
            for b, j in enumerate(f_flag):
                if self.comp(i, j):

                    key = font_parse_order[b].replace('uni', '')
                    key = eval(r'u"\u' + str(key) + '"').lower()
                    result_dict[key] = font_dict[a]
        return result_dict

    def comp(self,L1, L2):

        if len(L1) != len(L2):
            return 0
        for i in range(len(L2)):
            if L1[i] == L2[i]:
                pass
            else:
                return 0
        return 1
if __name__ == '__main__':
    t = TCSpider()
    t.get_data()