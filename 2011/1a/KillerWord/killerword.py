#!/usr/bin/python

import sys
from collections import deque

def solve(filename):
    fin = open(filename, "r")
    fout = open(filename[:-2] + "out", "w")
    case_count = int(fin.readline())
    for i in xrange(case_count):
        line = fin.readline().strip()
        result = process_case(parse_case(line, fin))
        output = 'Case #%d: %s' % (i+1, result)
        print(output)
        fout.write(output + '\n')
        
def parse_case(line, fin):
    pieces = line.split()
    n = int(pieces[0])
    m = int(pieces[1])
    
    words = {}
    for i in xrange(n):
        word = fin.readline().strip()
        len = len(word)
        if len not in words:
            words[len] = []
        words[len].append(word)
        
    lists = ''
    for i in xrange(m):
        lists += fin.readline().strip()
        
    return words, lists

def process_case(case):
    words, lists = case
    
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"
        
    solve(filename)