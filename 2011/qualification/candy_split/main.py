#!/usr/bin/python
import sys
from candy_split import *


if len(sys.argv) == 1:
    filename = "sample.txt"
else:
    filename = sys.argv[1]

run(filename)
