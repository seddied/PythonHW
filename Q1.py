input_as_str = raw_input("Please enter a number: ")
divided_by_3_counter = 0
for i in input_as_str:
    if (i == "-"):
        continue
    divided_by_3_counter += int(int(i) % 3 == 0)
print divided_by_3_counter


