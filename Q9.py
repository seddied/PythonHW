matrix = [[-4, 5, 3, 3.2], [5, 6.0, -2.4, 6], [7, 3, 2, -1]]
#matrix=[[-42]]
num_of_columns = len(matrix[0])
max_avg = 0
max_avg_index = 0
for i in range(num_of_columns):
    avg = float(sum([matrix[j][i] for j in range(len(matrix))]))/len(matrix)
    if max_avg_index== 0 or max_avg < avg:
        max_avg_index=i+1
        max_avg=avg

print(max_avg_index)


