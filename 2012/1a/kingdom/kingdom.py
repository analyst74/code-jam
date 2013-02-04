#!/usr/bin/python

import sys


def solve(filename):
    fin = open(filename, "r")
    fout = open(filename[:-2] + "out", "w")
    case_count = int(fin.readline())
    for i in xrange(case_count):
        #print ''
        #print 'case: ', i+1
        result = process_case(parse_case(fin))
        output = 'Case #%d: %s' % (i+1, result)
        print(output)
        fout.write(output + '\n')
        
def parse_case(fin):
    n = int(fin.readline())
    levels = []
    for i in xrange(n):
        pieces = fin.readline().split()
        s1 = int(pieces[0])
        s2 = int(pieces[1])
        levels.append((s1, s2))
    
    return n, levels
    
def process_case(case):
    #print case
    #print ''
    n, levels = case
    
    tier1 = {}
    tier2 = {}
    tier3 = {}
    for i in xrange(n):
        tier1[i] = levels[i][1]
        tier3[i] = levels[i][0]
    run = 0
    star = 0
    success = True
    
    while len(tier1) > 0 or len(tier2) > 0:
        #print tier1
        #print tier2
        #print tier3
        picks = [i for i in tier1 if star >= tier1[i]]
        if len(picks) > 0:
            del tier1[picks[0]]
            star += 2
            del tier3[picks[0]]
            #print('popping tier1 [%d]' % picks[0])
        else:
            picks = [i for i in tier2 if star >= tier2[i]]
            if len(picks) > 0:
                del tier2[picks[0]]
                star += 1
                #print('popping tier2 [%d]' % picks[0])
            else:
                picks = [i for i in tier3 if star >= tier3[i]]
                if len(picks) > 0:
                    best_pick = picks[0]
                    for p in picks:
                        if tier1[p] > tier1[best_pick]:
                            best_pick = p
                            
                    del tier3[best_pick]
                    star += 1
                    tier2[best_pick] = tier1.pop(best_pick)
                    #print('popping tier3 [%d]' % best_pick)                    
                else:
                    success = False
                    break
        run += 1
                    
    return run if success else "Too Bad"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"
        
    solve(filename)