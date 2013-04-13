__author__ = 'Bill'

from find_palindrome import find_all_palindromes, is_palindrome_reverse
from time import clock
from math import sqrt


def generate_palindromes(right=1000):
    result = [i for i in range(10) if i <= right]
    base_right = int(sqrt(right))

    for i in range(1, base_right):
        i_str = str(i)
        pal = int(i_str + i_str[::-1])
        if pal <= right:
            result.append(pal)
            if int(i_str + '0' + i_str[::-1]) <= right:
                for i in range(10):
                    pal = int(i_str + str(i) + i_str[::-1])
                    if pal <= right:
                        result.append(pal)

    return sorted(result)


def get_square_palindromes(pal_list, left, right):
    result = []
    for pal in pal_list:
        square = pal ** 2
        if square > right:
            break
        if left <= square and is_palindrome_reverse(square):
            result.append(square)

    return result


if __name__ == '__main__':
    left = 0
    right = 10 ** 11
    t0 = clock()
    all_pals = generate_palindromes(right)
    t1 = clock()
    square_pals = get_square_palindromes(all_pals, left, right)
    t2 = clock()
    found_pals = []
    if right <= 10 ** 6:
        found_pals = find_all_palindromes(left, right)
    t3 = clock()

    print(len(all_pals))
    print('execution time %s' % str(t1 - t0))
    print(len(square_pals), square_pals)
    print('execution time %s' % str(t2 - t1))
    if len(found_pals) > 0:
        print(len(found_pals), found_pals)
        print('execution time %s' % str(t3 - t0))

