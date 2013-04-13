__author__ = 'Bill'

import numpy

def parse_case(file):
    n, m = map(int, file.readline().split())
    print(n, m)
    lawn_map = []
    for i in range(n):
        row = list(map(int, file.readline().split()))
        lawn_map.append(row)

    return numpy.array(lawn_map)

def process_case(case):
    lawn_map = case
    unique_heights = sorted(set(lawn_map.ravel()))

    for h in unique_heights:
        if not test_validity(lawn_map, h):
            return 'NO'

    return 'YES'

def test_validity(lawn_map, h):
    n, m = lawn_map.shape

    spots = []

    for i in range(n):
        for j in range(m):
            if lawn_map[i,j] == h:
                if any(lawn_map[i, :] > h) and any(lawn_map[:, j] > h):
                    return False

    return True
