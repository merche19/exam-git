def from_decimal(number, base):  # перевод целого десятичного числа в любую СС
    result = ''
    while number >= base:
        result += str(number % base)  # получаем остаток от деления на каждой
        # итерации и результат записывается в строку
        number //= base  # это действие фактически меняет счетчик - получаем
        # результат от деления на каждой итерации и если условие цикла
        # удовлетворено, далее ищем остаток от деления
    if number // base < base:  # после завершения цикла к result добавляется
        # остаток от деления
        result += str(number)
    return result[::-1]  # строка переворачивается согласно правилу


print(from_decimal(101, 7))

# from_decimal переводит целое десятичное число в любую систему счисления
# результат - в виде строки


def sum_at_once(x, base):
    s = 0
    while x:
        s += x % base
        x //= base
    return s


print(sum_at_once(101, 7))

# sum_at_once СРАЗУ суммирует цифры числа, получившегося при
# переводе из десятичного числа в другую систему счисления


def sum_digits(integer):

    num = int(integer)
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    return sum


print("The sum of the digits is: ", sum_digits(38904))

# sum_digits просто суммирует цифры целого десятичного числа
