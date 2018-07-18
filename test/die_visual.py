from die import Die
import pygal


die = Die(6)
results = []
for roll_num in list(range(1000)):
    result = die.roll()
    results.append(result)

# print(results)

frequencies = []
for val in list(range(1, die.num_sides+1)):
    freq = results.count(val)
    frequencies.append(freq)

print(frequencies)

hist = pygal.Bar()
hist.title = 'results'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
