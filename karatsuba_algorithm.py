import sys

num_1 = int(sys.argv[1])
num_2 = int(sys.argv[2])
number_of_digits = int(sys.argv[3])


def multiply_two_numbers_karatsuba(x, y, n):
    """

    :param x: Integer x with n digits.
    :param y: Integer y with n digits
    :param n: Number of digits.
    :return: Product of integers x and y.

    x = 10^n/2*a + b
    y = 10^n/2*c + d
    Base Algorithm is x*y = 10^n(ac) + 10^n/2(ad+bc) + bd

    Use recursion to calculate them efficiently.

    """
    a, b = split_numbers(x, n)
    c, d = split_numbers(y, n)
    # print('{} {} {} {} {}'.format(a, b, c, d, n))
    if n == 2:
        # print((10**2 * a * c) + (a*d + c*b) * 10 + (b * d))
        return int((10 ** 2 * a * c) + (a * d + c * b) * 10 + (b * d))
    else:
        ac = multiply_two_numbers_karatsuba(a, c, n // 2)
        bd = multiply_two_numbers_karatsuba(b, d, n // 2)
        bc = multiply_two_numbers_karatsuba(b, c, n // 2)
        ad = multiply_two_numbers_karatsuba(a, d, n // 2)
        # print(10**n * ac + 10 * (ad + bc) + bd)
        return int(10 ** n * ac + 10 ** (n / 2) * (ad + bc) + bd)


def split_numbers(x, n):
    """

    :param x: Integer x with n digits
    :param n: Number of digits
    :return: return two numbers a and b split in the way x = 10^n/2*a + b
    """
    a = x // (10 ** (n // 2))
    b = x % (10 ** (n // 2))

    return int(a), int(b)


print(multiply_two_numbers_karatsuba(num_1, num_2, number_of_digits))
