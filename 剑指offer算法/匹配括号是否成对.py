import re
dict_bracket = {'}':'{',')':'(',']':'['}
brace_l = dict_bracket.values()
brace_r = dict_bracket.keys()

def check_brack(s):
    arr = []
    for i in range(len(s)-1):
        if s[i] in brace_l:
            arr.append(s[i])
        elif s[i] in brace_r:
            if arr and arr[-1] == dict_bracket[s[i]]:
                arr.pop()
            else:
                return False
    else:
        if len(arr) > 0:
            return False
        else:
            return True

s = '(5*(9+6*(2-30)-(10/2))-4)*8'


def output_re(s):
    if check_brack(s):
        list_01 = []
        for i in range(len(s) - 1):
            if s[i] == '(':
                list_01.append(i)
            elif s[i] == ')':
                l_index = list_01.pop()
                print(s[l_index:i + 1])
    else:
        print('不合法')

output_re(s)

