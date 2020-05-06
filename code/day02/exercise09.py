"""
温度换算

"""
# 获取华氏度，计算摄氏度
fahrenheit = float(input("请输入华氏度： "))
celsius = (fahrenheit - 32) / 1.8
print("摄氏度为：", celsius)

# 获取摄氏度，计算华氏度
celsius = float(input("请输入摄氏度： "))
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)

# 计算开氏度
kelvin = celsius + 273.15
print(kelvin)