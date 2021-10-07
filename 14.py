def decimal(number, base):
    result = ''
    while number >= base:
        result += str(number % base)
        number //= base
    if number // base < base:
        result += str(number)
    return result[::-1]


print(decimal(245, 2))
