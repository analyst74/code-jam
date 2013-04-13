__author__ = 'Bill'

import sys, time

def generate_palindromes(right=1000):
    result = [i for i in range(10) if i <= right]
    right_str = str(right)
    base_right = int(right / (10 ** int(len(right_str)/2)))

    for i in range(1, base_right):
        i_str = str(i)
        pal = int(i_str + i_str[::-1])
        if pal <= right:
            result.append(pal)
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

def is_palindrome_reverse(s):
    s = str(s)
    return s == s[::-1]

def parse_case(file):
    a, b = map(int, file.readline().split())

    return a, b


def process_case(case):
    a, b = case
    all_pals = generate_palindromes(b)
    square_pals = get_square_palindromes(all_pals, a, b)
    #print(all_pals, square_pals)
    return len(square_pals)

if __name__ == '__main__':
    t0 = time.clock()
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"

    input_file = open(filename, "r")
    output_file = open(filename.replace('in','out'), "w")
    case_count = int(input_file.readline())
    for i in range(case_count):
        result = process_case(parse_case(input_file))
        output_line = 'Case #%d: %s\n' % (i+1, result)
        print(output_line)
        output_file.writelines(output_line)

    input_file.close()
    output_file.close()

    print('Total Time: %s' % str(time.clock() - t0))