def number_to_words(num):
    ones = ['нуль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    return ones[num]

valid_numbers = []
with open('num.txt', 'r') as file:
    for line in file:
        for number in line.split():
            number = int(number, 16)  # преобразование из шестнадцатеричной системы в десятичную
            num_str = hex(number)[2:]  # строковое представление шестнадцатеричного числа
            if len(num_str) == int(num_str[0]) and number % 2 == 0 and number <= 0xC730:
                valid_numbers.append(number)
if valid_numbers:
    max_number = max(valid_numbers)
    max_number_words = " ".join([number_to_words(int(digit, 16)) for digit in hex(max_number)[2:]])
    print(f"Максимальное число: {max_number}, прописью: {max_number_words}")
else:
    print("Подходящих чисел не найдено")

if valid_numbers:
    print("Подходящие числа:")
    for number in valid_numbers:
        num_str = hex(number)[2:]
        print(number, ",".join([number_to_words(int(digit, 16)) for digit in num_str]))
    print(f"Количество подходящих чисел: {len(valid_numbers)}")