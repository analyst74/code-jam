__author__ = 'Bill'

import sys

def process_case(case):
    a, b = case
    pairs = set()

    for i in xrange(a, b):
        str_i = str(i)
        for j in xrange(len(str_i)):
            str_i = str_i[-1:] + str_i[:-1]
            int_i = int(str_i)
            if int_i > i and int_i >= a and int_i <= b:
                pairs.add('%d, %d' % (i, int_i))


    return len(pairs), pairs


zeros = 1
#a = 10**zeros
#b = 10**(zeros+1) - 1
a = 10
b = 20
result, pairs = process_case([a, b])
print('result for %s' % str([a,b]))
print('total count: %d' % result)
print pairs
