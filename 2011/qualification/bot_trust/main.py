#!/usr/bin/python
import sys
from bot_trust import *

if len(sys.argv) == 1:
    filename = "sample.txt"
else:
    filename = sys.argv[1]

case_list = get_data(filename)

i = 0
for case in case_list:
    i += 1
    step_count = process_case(case)
    print('Case #{0}: {1}'.format(i, step_count))