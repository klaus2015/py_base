def verify_permission(func):
    def wrapper(*args,**kwargs):
        print("权限验证")
        func(*args,**kwargs)

    return wrapper



# enter_background = verify_permission(enter_background)
@verify_permission
def enter_background(login_id, pwd):
    print("进入后台")
# delete_order = verify_permission(delete_order)
@verify_permission
def delete_order(name,id):
    print("删除订单")






enter_background("abc",1234)
delete_order("zs",333)