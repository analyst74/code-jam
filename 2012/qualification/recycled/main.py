#!/usr/bin/python

import sys
from recycled import *

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "sample.in"

run(filename)