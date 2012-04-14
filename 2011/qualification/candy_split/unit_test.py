#!/usr/bin/python

import unittest
from candy_split import patrick_add

class TestCandy(unittest.TestCase):

    def setUp(self):
        return
        
    def test_patrick_add(self):
        self.assertEqual(patrick_add('1100','0101'), '1001')
        self.assertEqual(patrick_add('1100','1001'), '0101')
        
if __name__ == '__main__':
    unittest.main()