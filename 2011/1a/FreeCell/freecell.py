#!/usr/bin/python

import sys

def solve(filename):
    fin = open(filename, "r")
    fout = open(filename[:-2] + "out", "w")
    case_count = int(fin.readline())
    for i in xrange(case_count):
        line = fin.readline()
        result = process_case(parse_case(line))
        output = 'Case #%d: %s' % (i+1, result)
        print(output)
        fout.write(output + '\n')
        
def parse_case(line):
    pieces = line.split()
    return int(pieces[0]), int(pieces[1]), int(pieces[2])

def process_case(case):
    n, pd, pg = case
            
    if pg == 100 and pd != 100 or pg == 0 and pd != 0:
        return "Broken"
    possible_d = 0
    while possible_d < n:
        possible_d += 1
        if possible_d * pd % 100 > 0:
            continue
            
        return "Possible"        
        
    return "Broken"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"
        
    solve(filename)