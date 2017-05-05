l1 = [1,2,3]
l2 = [5,6,7,8,9,0]

min_length = min(len(l1), len(l2))
l = []

for i in range(min_length):
    l.append(l1[i])
    l.append(l2[i])

l=l+l1[min_length:]
l=l+l2[min_length:]

print(l)