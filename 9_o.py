num = int(input("введите число: "))
def nums (num):
    if 1<=num<=12:
        numerals = ['один', "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двеннадцать"]
        a = numerals[num-1]

    else:
        a = ('')
    return a
if __name__ == "__main__":
    print(nums(num))
    