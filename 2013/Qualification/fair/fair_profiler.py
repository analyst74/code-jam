__author__ = 'Bill'

import cProfile


cProfile.run("from generate_palindromes import generate_palindromes; generate_palindromes(10**10)")