#!/usr/bin/python

from collections import deque
import numpy as np

def run(filename):
    f = open(filename, "r")
    case_count = int(f.readline())
    for i in xrange(case_count):
        line = f.readline()        
        result = process_case(parse_case(line,f))
        print('Case #%d: %s' % (i+1, result))

def parse_case(line, f):
    pieces = deque(line.split())
    h = int(pieces.popleft())
    w = int(pieces.popleft())
    d = int(pieces.popleft())
    map = np.
    for i in xrange(h):
        map
        
def process_case(case):