a = int(input(''))
n = a
for i in range(a):
    a =n/3
    n =a
    if n == 1:
        print(True)
        break
if n != 1:
    print(False)
