#!/usr/bin/python

class Combinator:
    lists = []
    promotions = []
    def __init__(self, lists):
        self.lists = lists
        self.promotions = [len(l) for l in lists]        
        #print self.lists, self.promotions
        
    def get_all_combinations(self):
        finished = False
        indexes = [0 for p in self.lists]
        while not finished:
            #print indexes
            if len(indexes) == len(set(indexes)):
                yield self.get_value(indexes)
            self.add_index(indexes)
            finished = sum(indexes) == 0
            
    def get_value(self, indexes):
        if len(indexes) != len(self.lists):
            raise IndexError("invalid indexes")
            
        return [self.lists[i][indexes[i]] for i in xrange(len(indexes))]
        
    def add_index(self, indexes, pos=-1, step=1):
        if pos < 0:
            pos = pos + len(self.lists)
        
        indexes[pos] += step
        #raw_input(indexes)
        if indexes[pos] >= self.promotions[pos]:
            indexes[pos] = 0
            if pos != 0:
                self.add_index(indexes, pos-1, 1)
            