from Lecture3.is_good_name import *
import unittest

class GoodNameTests(unittest.TestCase):

	# Good Variables
    def test_name_t0(self) -> None:
        self.assertTrue(is_good_name("test"))
    def test_name_t1(self) -> None:
        self.assertTrue(is_good_name("good_var"))

	#Bad Variables
    def test_name_t2(self) -> None:
        self.assertFalse(is_good_name("0"))
    def test_name_t3(self) -> None:
        self.assertFalse(is_good_name("really_explanatory_variable_name"))
    def test_name_t5(self) -> None:
        self.assertFalse(is_good_name("LOUD_VAR"))

	#Invalid Argument
    def test_sheesh_gen_t3(self) -> None:
        self.assertRaises(ValueError, is_good_name, "")

if __name__ == '__main__':
    unittest.main()