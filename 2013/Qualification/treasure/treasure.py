__author__ = 'Bill'

import sys, time
from collections import OrderedDict, Counter

def parse_case(file):
    k, n = map(int, file.readline().split())
    keys = Counter(file.readline().split())
    chests = OrderedDict()
    for i in range(n):
        chests[i+1] = file.readline().split()

    return keys, chests

def process_case(case):
    keys, chests = case
    result = 'IMPOSSIBLE'

    if pre_check(keys, chests) and l2_pre_check(keys, chests):
        path = depth_search([], keys, chests)
        if not path is None:
            result = ' '.join([str(i) for i in path])

    return result

def pre_check(keys, chests):
    all_keys = keys.copy()
    required_keys = Counter([])
    for index in chests:
        chest = chests[index]
        required_keys = required_keys + Counter([chest[0]])
        all_keys = all_keys + Counter(chest[2:])

    for key in required_keys:
        if key not in all_keys or all_keys[key] < required_keys[key]:
            return False

    return True

def l2_pre_check(keys, chests):
    all_keys = keys.copy()
    remaining_chests = chests.copy()

    expanded = True
    while expanded:
        expanded = False
        for index in remaining_chests:
            chest = remaining_chests[index]
            if chest[0] in all_keys:
                all_keys += Counter(chest[2:])
                del remaining_chests[index]
                expanded = True
                break

    return len(remaining_chests) == 0

def depth_search(path, keys, chests):
    if len(chests) == 0:
        return path
    if len(keys) == 0 and len(chests) > 0:
        #print("Path Failed: " + str(path))
        return None

    for index in chests:
        chest = chests[index]
        #print(keys, chest)
        if chest[0] in keys:
            temp_chests = chests.copy()
            del temp_chests[index]
            temp_keys = keys - Counter([chest[0]]) + Counter(chest[2:])

            result_path = depth_search(path + [index], temp_keys, temp_chests)
            if not result_path is None:
                return result_path

    return None

if __name__ == '__main__':
    t0 = time.clock()

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"

    input_file = open(filename, "r")
    output_file = open(filename.replace('in','out'), "w")
    case_count = int(input_file.readline())
    for i in range(case_count):
        result = process_case(parse_case(input_file))
        output_line = 'Case #%d: %s\n' % (i+1, result)
        print(output_line)
        output_file.writelines(output_line)

    input_file.close()
    output_file.close()

    print('Total Time: %s' % str(time.clock() - t0))