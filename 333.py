def is_divide(number1, number2):
    result = 0
    for n in range(number1, number2):
        if n % 20 == 0:
            result += 1
    chance = (result / (number2 - number1))
    return round(chance, 2)

print(is_divide(100, 999))


'''Encuentre la probabilidad de que
un número de tres dígitos elegido al azar
es divisible por xx'''
