__author__ = 'Bill'

import sys, time, math

def parse_case(file):
    s = map(int, file.readline().split())

    return list(s)[1:]

def process_case(case):
    s = case
    result = [0 for si in s]
    x = sum(s)
    poverty_indexes = []
    poverty_s = []
    for i in range(len(s)):
        l = s[i]
        throw_away_y = [(l-si)/x for si in s if si <= l]
        if sum(throw_away_y) >= 1:
            result[i] = 0
        else:
            poverty_indexes.append(i)
            poverty_s.append(l)

    poverty_buff = []
    lm = max(poverty_s)
    for l in poverty_s:
        poverty_buff.append((lm-l)/x)

    all_buff = sum(poverty_buff)
    mdiff = (1-all_buff)/len(poverty_indexes)
    for i in range(len(poverty_indexes)):
        result[poverty_indexes[i]] = poverty_buff[i] + mdiff

    #result.append((1-sum(throw_away_y)) / len(throw_away_y) * 100)

    return ' '.join(['%.5f' % (r*100) for r in result])



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