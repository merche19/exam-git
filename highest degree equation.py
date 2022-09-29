def find_roots(*args):

    roots = ''
    for x in args:
        result = (x ** 4) - (2 * x ** 3) - (3 * x ** 2) + (6 * x)
        if result == 0:
            roots += str(x) + '; '
    return roots


print(find_roots(0, 2))

# find the real roots for highest degree equation

