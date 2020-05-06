"""
三色球问题
"""
# 红球一个，黄球一个，绿球六个
for red in list(range(0,4)):
    for yellow in list(range(0,4)):
        for blue in list(range(0,7)):
            if red + yellow + blue == 8:
                print("红球%d个，黄球%d个，绿球%d个" % (red, yellow, blue))

# list_red = list(range(0, 4))
# list_yellow = list(range(0, 4))
# list_green = list(range(0, 7))
# if list_red[red] + list_yellow[yellow] + list_green == 8:
#     print("红球%d个，黄球%d个，绿球%d个" % (red, yellow, blue))