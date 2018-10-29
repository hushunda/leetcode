'''
Given a 32-bit signed integer, reverse digits of an integer.
'''


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    ma = 2 ** 31
    if x == 0:
        return x
    if x < 0:
        x = -x
        flag = -1

    else:
        flag = 1
    out = ''
    while x > 0:
        out = out + str(x % 10)
        x = x // 10
    out = flag * int(out)
    if (flag > 0) &(out > ma - 1):
        return 0
    elif (flag < 0) & (-out > ma):
        return 0
    else:
        return out


print(reverse(1534236469))