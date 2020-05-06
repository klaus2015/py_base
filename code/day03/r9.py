"""

根据身高体重,参照BMI,返回身体状况.
"""
while True:
    weight = float(input("请输入你的体重： "))
    hight = float(input("请输入你的身高"))
    BMI = weight / (hight **2)
    if BMI <18.5:
        print("体重过轻！")
    elif BMI <24:
        print("体重正常。")
    elif BMI < 28:
        print("超重")
    elif BMI < 30:
        print("I度肥胖。")
    elif BMI < 40:
        print("II度肥胖。")
    elif BMI >= 40:
        print("III度肥胖。")