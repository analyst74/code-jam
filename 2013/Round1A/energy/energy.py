__author__ = 'Bill'

import sys, time, math

def parse_case(file):
    e, r, n = map(int, file.readline().split())
    v = map(int, file.readline().split())

    return e, r, list(v)

def process_case(case):
    e, r, v = case
    #print(e, r, v)
    steps = int(math.ceil(e/r)) + 1

    gain = calc_gain(e, r, v, steps, [e for i in v])

    return gain


def calc_gain(e, r, v, steps, max_spend):

    gain = 0
    largest = max(v)
    index = v.index(largest)
    gain += largest * max_spend[index]

    v_left = v[:index]
    if len(v_left) > 0:
        max_spend_left = max_spend[:index]
        for i in range(steps):
            n = i+1
            if n > len(max_spend_left):
                break
            if n * r >= max_spend_left[-n]:
                break
            max_spend_left[-n] = n * r

        gain += calc_gain(e, r, v_left, steps, max_spend_left)

    v_right = v[index+1:]
    if len(v_right) > 0:
        max_spend_right = max_spend[index+1:]
        for i in range(steps):
            n = i+1
            if n > len(max_spend_right):
                break
            if n * r >= max_spend_right[i]:
                break
            max_spend_right[i] = n * r

        gain += calc_gain(e, r, v_right, steps, max_spend_right)

    return gain

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