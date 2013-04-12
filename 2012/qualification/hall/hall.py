#!/usr/bin/python

from collections import deque
import numpy as np

def solve(filename):
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
    # save the map
    map = [][]
    for i in range(h):
        row = f.readline()
        for j in range(w):
            map[i][j] = row[j]

    return map, h, w, d
        
def process_case(case):
    map, h, w, d = case

    # figure out how many duplications we need for each side
    hp = d / h / 2 + 1
    wp = d / w / 2 + 1

    # create mirrors of the map, and combine them
    fullMap = [[]*(wp*2*w+1) for i in range(hp*2*h+1)]
    for i in range(hp):



    # find the center me (among all the me's)

    # find all other me's within d of center me
    # and create rays between each of them to center me

    # deduct the rays crossing any mirror square

    # deduct stacked rays

    # return remaining number of rays, which is how many reflections we can see


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"

    solve(filename)