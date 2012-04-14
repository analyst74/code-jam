#!/usr/bin/python


def run(filename):
    f = open(filename, "r")
    case_count = int(f.readline())
    for i in xrange(case_count):
        line = f.readline()
        result = process_case(parse_case(line))
        print('Case #%d: %s' % (i+1, result))

def parse_case(line):
    pieces = line.split()    
    return int(pieces[0]), int(pieces[1])

def process_case(case):
    a, b = case
    result = 0
    tested_number = set()
    all_pairs = []
    for i in xrange(a, b):
        str_i = str(i)
        pairs = set([i])
        for j in xrange(len(str_i)):
            str_i = str_i[-1:] + str_i[:-1]
            int_i = int(str_i)
            if int_i > i and int_i >= a and int_i <= b:
                pairs.add(int_i)

        #print pairs
        result += len(pairs) - 1
        
    return result