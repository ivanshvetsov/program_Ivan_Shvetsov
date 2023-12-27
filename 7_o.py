def count_squares(A, B, C):
    squares_a = A // C
    squares_b = B // C
    total_squares = squares_a * squares_b
    return total_squares

A = int(input("Введите сторону большого прямоугольника А:"))
B = int(input("Введите сторону большого прямоугольника В:"))
C = int(input("Введите сторону маленького квадрата:"))
result = count_squares(A, B, C)
print("Количество маленьких квадратов поместившихся в большой прямоугольник:", result)