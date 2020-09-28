import unittest
from src.__init__ import *

# Classes with Unit Tests must inherit from unittest.TestCase
# Method test cases must start with test_
class NoArgumentTests(unittest.TestCase):
    def test_zeroCs(self):
        self.assertEqual(noArgument(), "This program accepts a varying number of command-line arguments and preforms actions based on the number of arguments provided. If you input zero arguments, the program will output this usage text. If you input one argument, the program will output whether the argument is even, odd, or not an integer. If you input more than one argument, the program will output the number of c's (case insensitive) in the arguments.")

class OneArgumentTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(oneArgument('0'), 'Zero')
    def test_odd(self):
        self.assertEqual(oneArgument('1'), 'Odd')
    def test_even(self):
         self.assertEqual(oneArgument('2'), 'Even')
    def test_checkIfInt(self):
        self.assertEqual(oneArgument('3.14'), 'Not An Integer')

class MultiArgumentTests(unittest.TestCase):
    def test_zeroCs(self):
        self.assertEqual(multiArgument('Joey, have you ever been in a Turkish prison?'), 0)
    def test_oneC(self):
        self.assertEqual(multiArgument('This has one c'), 1)
    def test_twoCs(self):
        self.assertEqual(multiArgument('Can I interest you in a nightcap?  No thank you, I dont wear them'), 2)

if __name__ == "__main__":
    unittest.main()