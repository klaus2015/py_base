def add_permission(func):
    def wrapper(*args, **kwargs):
        print("增加权限验证")
        return func(*args, **kwargs)
    return wrapper




def deposit(money):
    print("存%d钱喽" % money)

@add_permission
def withdraw(login_id,pwd):
    print("取钱喽",login_id,pwd)


deposit(10000)
withdraw("zs",123)