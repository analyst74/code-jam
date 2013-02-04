#!/usr/bin/python

class ScoreCache:    
    cache = dict()

    def add(self, hand, turn, deck_size, score):
        key = '%d%d%d' % (len(hand), turn, deck_size)
        if not key in self.cache:
            self.cache[key] = []
        self.cache[key].append([(hand, turn, deck_size), score])

    def get(self, hand, turn, deck_size):
        key = '%d%d%d' % (len(hand), turn, deck_size)
        if key in self.cache:
            for real_key, score in self.cache[key]:
                if set(hand) == set(real_key[0]) and \
                    turn == real_key[1] and \
                    deck_size == real_key[2]:
                    return score
        return -1

    def contains(self, hand, turn, deck_size):
        return self.get(hand, turn, deck_size) > -1
