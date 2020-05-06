"""
We are happy! 输出成  We%20are%20happy%20are!

"""



s = 'We are happy are !'
def replace(s):
    s1 = ''
    for i in s:
        if i == ' ':
            s1 += '20%'
        else:
            s1 += i
    print(s1)
replace(s)

def replace_2(s):
    if type(s) != str:
        return
    return s.replace(' ','20%')

print(replace_2(s))
print(s)