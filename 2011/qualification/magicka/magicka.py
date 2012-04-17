#!/usr/bin/python
from collections import deque

def run(filename):
    f = open(filename, 'r')
    case_count = int(f.readline())
    case_list = []
    for i in xrange(case_count):
        button_list = []
        line = f.readline()
        #print
        #print(line[:-1])
        result = process_case(parse_case(deque(line.split())))
        display_result = '['
        for c in result:
            display_result += c + ', '
        if len(display_result) > 1:
            display_result = display_result[:-2]
        display_result += ']'
        print('Case #%d: %s' % (i+1, display_result))
        
    f.close()
    return case_list
    
def parse_case(pieces):
    combo_list = []
    combo_count = int(pieces.popleft())
    for i in xrange(combo_count):
        str = pieces.popleft()
        combo_list.append(((str[0],str[1]),str[2]))
        
    oppo_list = []
    oppo_count = int(pieces.popleft())
    for i in xrange(oppo_count):
        str = pieces.popleft()
        oppo_list.append((str[0],str[1]))
        
    element_list = pieces.pop()
    element_list = list(element_list)
    return (combo_list, oppo_list, element_list)
    
def process_case(case):
    combo_list, oppo_list, element_list = case
    result = []
    i = 0
    while i < len(element_list):
        result.append(element_list[i])
        
        process_combo(combo_list, result)
        #print(result)
        
        for key in oppo_list:
            if result[-1] in key:
                match_element = key[1] if key[0] == result[-1] else key[0]
                if match_element in result:
                    result = []
                    break
                    
        i += 1
    
    return result
    
def process_combo(combo_list, result):
    if len(result) < 2:
        return
        
    for key, value in combo_list:
        if set(key) == set((result[-1], result[-2])):
            result.pop()
            result.pop()
            result.append(value)
            return process_combo(combo_list, result)