#!/usr/bin/python

from collections import deque

def run(filename):
    f = open(filename, "r")
    case_count = int(f.readline())
    for i in xrange(case_count):
        line = f.readline()
        result = process_case(parse_case(line))
        print('Case #%d: %s' % (i+1, result))
  
def process_case(case):
    n, s, p, t = case
    
    #print n, t
        
    sure_match = [point for point in t if point >= 3 * p - 2 or p == 0]
    maybe_match = [point for point in t if point not in sure_match and point >= 3 * p - 4 and (p != 1 or point > 0)]
    
    #print sure_match, maybe_match, s
    return len(sure_match) + min(len(maybe_match), s)
    
def parse_case(line):
    pieces = deque(line.split())
    n = int(pieces.popleft())
    s = int(pieces.popleft())
    p = int(pieces.popleft())
    t = []
    for i in xrange(n):
        t.append(int(pieces.popleft()))
    return (n, s, p, t)