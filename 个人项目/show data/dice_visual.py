from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# print(results)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequencies.append(results.count(value))

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = list(range(2,max_result+1))
hist.x_title = 'Result'
hist.y_title = "Frequency of Result"
hist.add('D6 + D6',frequencies)
hist.render_to_file('die_visual.svg')