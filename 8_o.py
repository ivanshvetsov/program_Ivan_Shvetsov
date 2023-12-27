def calculate_taxi_payment(distance):
    baztarif = 240
    za140m = 15
    distance_in_140m = distance * 1000 / 140
    additional_fare = za140m * distance_in_140m
    itogsumma = baztarif + additional_fare
    return itogsumma
distance = int(input("Введите расстояние в километрах: "))
payment = calculate_taxi_payment(distance)
print("Итоговая сумма оплаты такси:", payment, "p.")
