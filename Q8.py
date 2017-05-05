l = ['','hi','bye','wow','bow','wawawiwa','b']
d = {}
for str in l:
    if (len(str) == 0):
        continue
    if (d.has_key(str[0])):
        d[str[0]].append(str[1:])
    else:
        d[str[0]] = [str[1:]]

print d