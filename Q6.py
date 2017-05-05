d = {'1': '2', 'a':'4', 'x':'4', 4:3, 2:2}

d_values = d.values()
d_values.sort()
max_count = 0
count = 0
max_value = 0
for i in range(len(d_values)):
    if i > 0 and d_values[i] != d_values[i-1]:
        if (count > max_count):
            max_count = count
            max_value = d_values[i-1]
        count = 0
    count+=1
if (count > max_count):
    max_count = count
    max_value = d_values[len(d_values)-1]

print(max_value)
