import re

f = open('b')

def set_str(s):
   """"去重"""
   list_re = []
   for item in s:
      if item not in list_re:
         list_re.append(item)
   return list_re

list_nums = []
for i in f:
    list_re = set_str(i.strip())
    result = ''.join(list_re)
    list_nums.append(int(result))
list_nums = sorted(list_nums,reverse=True)
print(list_nums)



# re = set_str(s)
# print(re)
# a = ''.join(re)
# print(a)







