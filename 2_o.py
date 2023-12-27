A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

count = 0
for i in range(A, B+1):
    print(i)
    count += 1

print("Количество чисел в диапазоне:", count)