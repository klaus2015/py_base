"""
已知：加速度，初速度，时间,求距离

"""
# 获取加速度
accelerated_speed = int(input("请输入加速度： "))
# 获取初速度
initial_velocity = int(input("请输初速度： "))
# 获取时间
time = int(input("请输入时间： "))
distance = accelerated_speed * time ** 2 *0.5 + initial_velocity * time
print("距离是", distance)