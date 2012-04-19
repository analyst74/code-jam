#!/usr/bin/python

import sys
from collections import namedtuple
from operator import attrgetter

Card = namedtuple('Card', 'c s t')

def solve(filename):
    fin = open(filename, "r")
    fout = open(filename[:-2] + "out", "w")
    case_count = int(fin.readline().strip())
    for i in xrange(case_count):
        result = process_case(parse_case(fin))
        output = 'Case #%d: %d' % (i+1, result)
        print(output)
        fout.write(output + '\n')
        
def parse_case(fin):
    n = int(fin.readline().strip())    
    hand_cards = []
    for i in xrange(n):
        pieces = fin.readline().split()
        hand_cards.append(Card(int(pieces[0]), int(pieces[1]), int(pieces[2])))
        
    m = int(fin.readline().strip())    
    deck_cards = []
    for i in xrange(m):
        pieces = fin.readline().split()
        deck_cards.append(Card(int(pieces[0]), int(pieces[1]), int(pieces[2])))
        
    return hand_cards, deck_cards

def process_case(case):
    hand_cards, deck_cards = case
    result = 0
    
    t = 1
    s = 0
    print len(hand_cards), 0, t
    while t > 0:
        t -= 1
        if len(hand_cards) > 0:
            hand_cards.sort(key=attrgetter('t', 'c', 's'), reverse=True)
            card = hand_cards.pop(0)
            t += card.t
            s += card.s
            for i in xrange(card.c):
                if len(deck_cards) > 0:
                    hand_cards.append(deck_cards.pop(0))
        
        print card, len(hand_cards), s, t
    
    print('remaining hand cards: %s' % (str(hand_cards)))
    return result
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"
        
    solve(filename)