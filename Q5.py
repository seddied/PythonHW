a = int(raw_input("Please input a: "))
b = int(raw_input("Please input b: "))
if b < a:
    print("b should be >= a")
    exit(1)

dict = dict([(i,i) for i in range(a,b+1)])
print(dict)