numbers = []

def is_even_and_hex(number):
    if number % 2 == 0 and len(hex(number)[2:]) == int(str(number)[0]):
        return True
    return False

with open('numbers.txt', 'r') as file:
    numbers_str = file.readline().split()
    numbers = [int(num) for num in numbers_str if num.isdigit()]


max_number = max(numbers)

def number_to_words(number):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    if number == 1000:
        return "тысяча"
    elif number >= 100:
        return units[number // 100] + "сто " + number_to_words(number % 100)
    elif number >= 20:
        return tens[number // 10] + " " + units[number % 10]
    elif number >= 10:
        return teens[number - 10]
    else:
        return units[number]
    print("Числа:")
for number in numbers:
    print(number, end=" ")
    print("\nКоличество чисел:", len(numbers))
    print("\nМаксимальное число: ", number_to_words(max_number))
