import sys

a = float(input('Введите сторону прямоугольника А '))
b = float(input('Введите сторону прямоугольника В '))
c = float(input('Введите число С '))
if a<=0 or b<=0 or c<=0:
    print('Ошибка. Число должно быть больше нуля.')
    sys.exit()

priamoug = a * b
kvadr = c ** 2
summ = priamoug
done = 0
while summ>= kvadr:
    summ -= kvadr
    done += 1
print('В прямоугольник AB поместятся',done,'квадратa(ов) со стороной С')
