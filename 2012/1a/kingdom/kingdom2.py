#!/usr/bin/python

import sys

HASH = 10000

def solve(filename):
    fin = open(filename, "r")
    fout = open(filename[:-2] + "out", "w")
    case_count = int(fin.readline())
    for i in xrange(case_count):
        result = process_case(parse_case(fin))
        output = 'Case #%d: %s' % (i+1, result)
        print(output)
        fout.write(output + '\n')
        
def parse_case(fin):
    n = int(fin.readline())
    levels = []
    for i in xrange(n):
        pieces = fin.readline().split()
        s1 = int(pieces[0])
        s2 = int(pieces[1])
        levels.append((s1, s2))
    
    return n, levels
    
def process_case(case):
    n, levels = case
    
    requirement = {}
    potentials = {}
    for i in xrange(n):
        potentials[i] = 1
        potentials[HASH+i] = 2
        requirement[i] = levels[i][0]
        requirement[HASH+i] = levels[i][1]
    
    
    
    lv1 = {}
    lv2 = {}
    for i in xrange(n):
        lv1[i] = levels[i][0]
        lv2[i] = levels[i][1]
        
    run = 0
    star = 0
    success = True
    
    while star < n * 2:
        doable_lv2 = {i:lv2[i] for i in lv2 if not completed[i][1] and star >= lv2[i]}
        if len(doable_lv2) > 0:
            fresh_lv2 = [i for i in doable_lv2 if not completed[i][0]]
            if len(fresh_lv2) > 0:
                
                
        run += 1
                    
    return run if success else "Too Bad"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"
        
    solve(filename)