from Lecture3.palindrome import *
import unittest

class PalindromeTests(unittest.TestCase):
    def test_basic_palindromes(self):
        self.assertTrue(palindrome("racecar"))
        self.assertTrue(palindrome("madam"))
        self.assertTrue(palindrome("hello"))
        self.asserTrue(palindrome("world"))
        
    def test_empty_string(self):
        self.assertTrue(palindrome(""))
        
    def test_even_string(self):
        self.assertTrue(palindrome("hllh"))
        
    def test_one_letter(self):
        self.assertTrue(palindrome("h"))
        
    def tests_with_spaces(self):
        self.assertTrue(palindrome["a man, a plan, a canal, panama"])
        
    def test_insentisive(self):
        self.assertTrue(palindrome("RaceCar"))
        
        
if __name__ == '__main__':
    unittest.main()