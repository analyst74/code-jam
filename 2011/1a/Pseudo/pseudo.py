#!/usr/bin/python

import sys
from collections import namedtuple
from operator import attrgetter
from ScoreCache import ScoreCache

Card = namedtuple('Card', 'c s t')

fin_count = 2

def solve(filename):
    global fin_count
    fin = open(filename, "r")
    fout = open(filename[:-2] + "out", "w")
    case_count = int(fin.readline().strip())
    for i in xrange(case_count):
        print 'process.start %d' % fin_count
        result = process_case(parse_case(fin))
        print 'process.end %d' % fin_count
        output = 'Case #%d: %d' % (i+1, result)
        print(output)
        fout.write(output + '\n')
        
def parse_case(fin):
    global fin_count
    n = int(fin.readline().strip())
    fin_count += 1
    hand = []
    for i in xrange(n):
        pieces = fin.readline().split()
        fin_count += 1
        hand.append(Card(int(pieces[0]), int(pieces[1]), int(pieces[2])))
        
    m = int(fin.readline().strip())
    fin_count += 1
    deck = []
    for i in xrange(m):
        pieces = fin.readline().split()
        fin_count += 1
        deck.append(Card(int(pieces[0]), int(pieces[1]), int(pieces[2])))

    return hand, deck

def process_case(case):
    hand, deck = case
    result = 0
    cache = ScoreCache()
    
    return simulate_turn(1, hand, deck, cache)

def play_easy_cards(hand, deck):
    easy_card = [card for card in hand if card.t > 0]
    if len(easy_card) == 0:
        return 0, 0, 0
    
    c = sum([card.c for card in easy_card])
    s = sum([card.s for card in easy_card])
    t = sum([card.t for card in easy_card]) - len(easy_card)

    for card in easy_card:
        hand.remove(card)
    for i in xrange(c):
        if len(deck) > 0:
            hand.append(deck.pop(0))
            
    next_c, next_s, next_t = play_easy_cards(hand, deck)

    return c + next_c, s + next_s, t + next_t

def simulate_turn(turn, hand, deck, cache):
    best_score = 0
    easy_score = 0
    if turn == 0:
        best_score = 0
    elif cache.contains(hand, turn, len(deck)):
        best_score = cache.get(hand, turn, len(deck))
        #print 'returning from cache...', 
        #print turn, len(hand), len(deck), best_score
    else:
        #print len(hand), len(deck)
        c, easy_score, t = play_easy_cards(hand, deck)
        #print len(hand), len(deck), t
        #raw_input()
        turn += t
        
        best_card_to_play = None        
        hand_count = len(hand)
        for i in xrange(hand_count):
            card = hand[i]
            next_hand = hand[:]
            next_hand.remove(card)
            next_deck = deck[:]
            for j in xrange(card.c):
                if len(next_deck) > 0:
                    next_hand.append(next_deck.pop(0))
            score = card.s + \
                simulate_turn(turn + card.t - 1, 
                              next_hand,
                              next_deck,
                              cache)
            if score >= best_score:
                best_score = score
                best_card_to_play = card
        cache.add(hand, turn, len(deck), best_score)
        
    return best_score + easy_score
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"
        
    solve(filename)
