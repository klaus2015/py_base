# dict_bracket = {'}': '{', ')': '(', ']': '[', '>': '<'}
# print(dict_bracket.keys())
# print(dict_bracket.values())
def check_brace(string):
    stack = []
    dict_bracket = {'}': '{', ')': '(', ']': '[', '>': '<'}
    for brace in string:
        if brace in dict_bracket.values():
            stack.append(brace)
        elif brace in dict_bracket.keys():
            if stack and dict_bracket[brace] == stack[-1]:
                stack.pop()
            else:
                return False
    else:
        if stack:
            return False
        else:
            return True
s = '(5*(9+6*(2-30)-(10/2))-4)*8'
a =  "([{ }]"
print(check_brace(a))
# dict_bracket = {'}':'{',')':'(',']':'['}
# brace_l = dict_bracket.values()
# brace_r = dict_bracket.keys()
# def check_brack(s):
#     arr = []
#     for i in range(len(s)-1):
#         if s[i] in brace_l:
#             arr.append(s[i])
#         elif s[i] in brace_r:
#             if arr and arr[-1] == dict_bracket[s[i]]:
#                 arr.pop()
#             else:
#                 return False
#     else:
#         if len(arr) > 0:
#             return False
#         else:
#             return True
# s = '(5*(9+6*(2-30)-(10/2))-4)*8'
# print(check_brack(s))
