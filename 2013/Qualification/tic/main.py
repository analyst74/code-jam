#!/usr/bin/python

import sys
from tic import *

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "sample.in"

f = open(filename, "r")
case_count = int(f.readline())
for i in range(case_count):
    result = process_case(parse_case(f))
    print('Case #%d: %s' % (i+1, result))