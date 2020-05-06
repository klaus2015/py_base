from fontTools.ttLib import TTFont
# 2292
new_str = ['&#xf4ea','&#xf4ea','&#xf2bd','&#xe4e3'] # 1125

# 2276
font_dic = [{'uniE951':7},{'uniE6E5':0},{'uniE783':5},{'uniF3C3':6},{'uniEBA2':9},
            {'uniE0BB':1},{'uniED1C':8},{'uniEE52':2},{'uniF7C7':3},{'uniEA7B':4},]
u_list = ['uniE951','uniE6E5','uniE783','uniF3C3','uniEBA2','uniE0BB','uniED1C','uniEE52','uniF7C7','uniEA7B']
word_list = [7,0,5,6,9,1,8,2,3,4]
# 2276
font_base = TTFont('font_base.woff')
font_base_order = font_base.getGlyphOrder()[2:]

be_p1=[] #保存10个字符的（x,y）信息
for i in font_base_order:
    p1 = []
    p = font_base['glyf'][i].coordinates
    for f in p:
        p1.append(f)
    be_p1.append(p1)
print(be_p1)
print(len(be_p1))

# 2292
font_new = TTFont('font_new.woff')
font_new_order = font_new.getGlyphOrder()[2:]
new_p1=[] #保存10个字符的（x,y）信息
for i in font_new_order:
    p1 = []
    p = font_new['glyf'][i].coordinates
    for f in p:
        p1.append(f)
    new_p1.append(p1)
print(new_p1)
print(len(new_p1))
# print(font_base['glyf'][font_base_order[0]])
# base = font_base['glyf'][font_base_order[0]]
# print(base.coordinates)
# print(base.coordinates[1])


def comp(l1, l2):  # 定义一个比较函数，比较两个列表的坐标信息是否相同
    if len(l1) != len(l2):
        return False
    else:
        mark = 1
        for i in range(len(l1)):
            if abs(l1[i][0] - l2[i][0]) < 40 and abs(l1[i][1] - l2[i][1]) < 40:
                pass
            else:
                mark = 0
                break
        return mark

# n2 = 0
# x_list1 = []
# for d in new_p1:
#     n2 += 1
#     n1 = 0
#     for a in be_p1:
#         n1 += 1
#         if comp(a,d):
#             print(font_new_order[n2-1],word_list[n1-1])
#             x_list1.append(word_list[n1-1])
# print(x_list1)

x_list = []
new_font_dic = {}
for i, d in enumerate(new_p1):
    for j, a in enumerate(be_p1):
        if comp(a,d):
            print(font_new_order[i],word_list[j])
            new_font_dic[font_new_order[i]]=word_list[j]
            x_list.append(word_list[j])

print(x_list)
print(new_font_dic)
score_str = ['&#xf573','&#xe79d'] # 7.4
for i in range(len(score_str)):
    score_str[i] = 'uni' + score_str[i].replace('&#x','').upper()
print(score_str)
