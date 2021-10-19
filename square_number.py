# Given an integral number, determine if it's a square number:

def if_square_number(x):
    if x <= 0:
        return False
    if x % 10 == 2 or 3 or 7 or 8:
        return False
    if x % 10 == 1:

print(if_square_number(27))


# 1, 4, 9, 6, 5, 6, 9, 4, 1, 0 last_dgt of square number
# 1, 2, 3, 4, 5,
# 9, 8, 7, 6,
#
