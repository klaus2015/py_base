from die import Die
import pygal

die = Die(6)

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# print(results)

# 分析结果
frequencies = []
for value in range(1,die.num_side+1):
    frequencies.append(results.count(value))

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(1,die.num_side+1))
hist.x_title = 'Result'
hist.y_title = "Frequency of Result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')