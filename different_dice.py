from die import Die
import pygal

# Создание кубиков D6 и D10.
die_1 = Die()
die_2 = Die()
die_3 = Die()
# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(5000):
    result = die_1.roll() * die_2.roll() * die_2.roll()
    results.append(result)
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    # Визуализация результатов.
    hist = pygal.Bar()
    hist.title = "Результаты бросков кубиков " + str(die_1.num_sides) + " + " + \
                 str(die_2.num_sides) + " + " + str(die_3.num_sides) +\
                 " = " + str(max_result) + " граней"
    labels = []
    for res in range(3, max_result + 1):
        x_labels = res
        labels.append(x_labels)
        hist.x_labels = labels
        # hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
        # '13', '14', '15', '16']
    hist.x_title = "Результаты"
    hist.y_title = "Количество бросков " + str(sum(frequencies))
    hist.add(str(die_1.num_sides) + ' + ' + str(die_2.num_sides) + ' + ' + str(die_3.num_sides),
             frequencies)
    hist.render_to_file('dice_visual.svg')
