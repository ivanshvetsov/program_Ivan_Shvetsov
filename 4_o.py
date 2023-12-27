A = int(input("Введите значение A: "))
B = int(input("Введите значение B (A < B): "))

sum_all = sum(range(A, B + 1))
sum_even = sum(range(A, B + 1, 2))
sum_odd = sum(range(A + 1, B + 1, 2))

print(f"Сумма всех чисел от {A} до {B}: {sum_all}")
print(f"Сумма четных чисел от {A} до {B}: {sum_even}")
print(f"Сумма нечетных чисел от {A} до {B}: {sum_odd}")