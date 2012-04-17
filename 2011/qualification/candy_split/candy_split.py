#!/usr/bin/python
from Combinator import Combinator

def run(filename):
    f = open(filename, 'r')
    case_count = int(f.readline())
    case_list = []
    for i in xrange(case_count):
        candy_count = int(f.readline())
        line = f.readline()
        all_candies = [bin(int(value))[2:] for value in line.split()]
        #print(all_candies)
        result = process_case(all_candies)
        
        print ('Case #%d: %s' % (i+1, result if result > 0 else 'NO'))
        
def process_case_v2(all_candies):
    # algorithm:
    # group candy by length of their value in bit
    # for each group, find all combinations
        # find all combinations of k items
        # start from 1, until k > n (n is total number of items in the group)        
    # find combinations of all groups combined
        # find the largest pile
        
    return

def process_case(all_candies):        
    result = -1
    max_k = len(all_candies) / 2
    
    for i in xrange(max_k):
        k = i + 1
        lists = []
        for i in xrange(k):
            lists.append(all_candies)
        c = Combinator(lists)
        for left_pile in c.get_all_combinations():
            
            right_pile = all_candies[:]
            [right_pile.remove(candy) for candy in left_pile]
            #print left_pile, patrick_sum(left_pile), right_pile, patrick_sum(right_pile)
            if patrick_sum(left_pile) == patrick_sum(right_pile): 
                result = max(result, normal_sum(left_pile), normal_sum(right_pile))
    
    return result
    
def normal_sum(list):
    result = 0
    for item in list:
        result += int(item, base=2)
        
    return result
    
def patrick_sum(list):
    result = '0'
    for item in list:
        result = patrick_add(result, item)
        
    return int(result, base=2)
    
def patrick_add(left, right):
    left = list(left)
    right = list(right)
    size = max(len(left), len(right))
    while(len(left) < size):
        left.insert(0,'0')
    while(len(right) < size):
        right.insert(0,'0')
    
    result = ''
    for i in xrange(size):
        result += '0' if left[i] == right[i] else '1'
        
    return result
    