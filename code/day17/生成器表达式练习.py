list01 = [1,"23",True,555,"大家",False,10,"abc",3.4]
def get_re(list_target):
    for item in list_target:
        if type(item) == str:
            yield item
re = get_re(list01)
for item in re:
    print(item)

re = (item for item in list01 if type(item) == str)
for item in re:
    print(item)
result = [item for item in list01 if type(item) == str]
for item in result:
    print(item)