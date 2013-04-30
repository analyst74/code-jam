__author__ = 'Bill'

import sys, time, math

def parse_case(file):
    r, t = map(int, file.readline().split())

    return r, t

def process_case(case):
    r, t = case

    n = math.sqrt(t/2*16 + (2*r - 1)**2) - (2*r -1)

    return int(n/4)

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