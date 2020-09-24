import unittest
import commandlinelab

# Classes with Unit Tests must inherit from unittest.TestCase
# Method test cases must start with test_
class MultiArgumentTests(unittest.TestCase):
    def test_zeroCs(self):
        self.assertEqual(commandlinelab.noArgument(), 'Usage')

class OneArgumentTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(commandlinelab.oneArgument('0'), 'Zero')
    def test_odd(self):
        self.assertEqual(commandlinelab.oneArgument('1'), 'Odd')
    def test_even(self):
        self.assertEqual(commandlinelab.oneArgument('2'), 'Even')
    def test_checkIfInt(self):
        self.assertEqual(commandlinelab.oneArgument('3.14'), 'Not An Integer')

class MultiArgumentTests(unittest.TestCase):
    def test_zeroCs(self):
        self.assertEqual(commandlinelab.multiArgument('Joey, have you ever been in a Turkish prison?'), '0')
    def test_oneC(self):
        self.assertEqual(commandlinelab.multiArgument('Tis but a scratch'), '1')
    def test_twoCs(self):
        self.assertEqual(commandlinelab.multiArgument('Can I interest you in a nightcap?  No thank you, I dont wear them'), '2')
    

