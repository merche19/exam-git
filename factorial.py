def count_factorial(number):  # calcular el factorial de un número

    if number <= 0:
        return 'not defined'

    elif str(number).isnumeric():

        i = number
        result = 1
        while i >= 1:
            result *= i
            i -= 1
        return result

    else:
        return 'not defined'


print(count_factorial(5))
