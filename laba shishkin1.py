def number_to_words(num):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
            "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    if num == 0:
        return "ноль"
    if num < 0:
        return "минус " + number_to_words(abs(num))
    result = ""
    if num >= 1000:
        result += number_to_words(num // 1000) + " тысяч "
        num %= 1000
    if num >= 100:
        result += hundreds[num // 100] + " "
        num %= 100
    if num >= 10:
        if num >= 20:
            result += tens[num // 10] + " "
            num %= 10
        else:
            result += units[num] + " "
            num = 0
    if num > 0:
        result += units[num]
    return result
count = 0
for i in range(8, 204810):
    hex_num = hex(i)[2:]
    if len(hex_num) == str(hex_num)[0]:
        decimal_num = int(hex_num, 16)
        if decimal_num % 2 == 0:
            count += 1
            print(hex_num)
max_num_in_words = number_to_words(int(hex_num, 16))
print("Количество чисел:", count)
print("Максимальное число прописью:", max_num_in_words)
