#!/usr/bin/python

import sys


def solve(filename):
    fin = open(filename, "r")
    fout = open(filename[:-2] + "out", "w")
    case_count = int(fin.readline())
    for i in xrange(case_count):
        result = process_case(parse_case(fin))
        output = 'Case #%d: %f' % (i+1, result)
        print(output)
        fout.write(output + '\n')
        
def parse_case(fin):
    pieces = fin.readline().split()
    a = int(pieces[0])
    b = int(pieces[1])
    
    prob = []
    pieces = fin.readline().split()
    for piece in pieces:
        prob.append(float(piece))
        
    return a, b, prob
    
def process_case(case):
    a, b, prob = case
    
    expected = []
    # give up
    expected.append(b + 2)
    # keep typing
    p_no_error = get_prod(prob[:a])
    expected.append((b+1-a)*p_no_error + (2*b+2-a)*(1-p_no_error))
    
    prev_prod = p_no_error
    for i in xrange(a):
        n = i + 1
        remaining = a - n
        p_no_error = prev_prod / prob[a-n]
        prev_prod = p_no_error
        expected.append((2*n+b+1-a)*p_no_error + (2*n+2*b+2-a)*(1-p_no_error))
        
    return min(expected)
        
def get_prod(list):
    prod = 1
    for p in list:
        prod *= p
    
    return prod
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"
        
    solve(filename)