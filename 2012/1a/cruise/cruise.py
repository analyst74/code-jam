#!/usr/bin/python

import sys, math


def solve(filename):
    fin = open(filename, "r")
    fout = open(filename[:-2] + "out", "w")
    case_count = int(fin.readline())
    for i in xrange(case_count):
        #print ''
        #print 'case: ', i+1
        result = process_case(parse_case(fin))
        output = 'Case #%d: %s' % (i+1, result)
        print(output)
        fout.write(output + '\n')
        
def parse_case(fin):
    n = int(fin.readline())
    cars = []
    for i in xrange(n):
        pieces = fin.readline().split()
        s = int(pieces[1])
        p = int(pieces[2])
        cars.append((s, p))
    
    return n, cars
    
def process_case(case):
    #print case
    #print ''
    n, cars = case
    
    passing = []
    for i in xrange(n):
        for j in xrange(i+1, n):
            s1 = cars[i][0]
            p1 = cars[i][1]
            s2 = cars[j][0]
            p2 = cars[j][1]
            
            if s1 == s2 and math.abs(p1-p2) - 5 < 0:
            
            t1 = (p2-(p1+10)) / (s1-s2)
            t2 = ((p2+10)-p1) / (s1-s2)
            if t1 >= 0 and t2 >= 0:
                passing.append((min(t1, t2), max(t1, t2)))
        
    p_count = len(passing)
    passing.sort()
    for i in xrange(p_count):
        for j in xrange(p_count):
            if passing[i][0] >= passing[j][0] and passing[i][0] < passing[j][1]:
                return passing[i][0]
                
    return "Possible"
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"
        
    solve(filename)