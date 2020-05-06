"""
    定义函数，计算指定范围内的素数 只能被一和自身整除的数

"""
def get_prime(min, max):
    result = []
    for number in range(min,max):
        if is_prime(number): # 如果返回真值,则添加进列表中
            result.append(number)
    return result
    # return [number for number in range(min,max) if is_prime(number)]

def is_prime(number):
    for item in range(2, number):
        if number % item == 0:
            return False
        else:
            return True   # 不进到return False 说明是素数,返回真值


print(get_prime(3,10))


