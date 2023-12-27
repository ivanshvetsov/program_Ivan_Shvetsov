cena_za_kg = float(input("Введите цену 1 кг конфет:"))
for ves in range(12, 21, 2):
    ves_kg = ves / 10.0  
    stoimost = cena_za_kg * ves_kg
    print(f"Стоимость {ves_kg} кг конфет: {stoimost} р.")