from burnymon import *
import unittest

class BurnymonTests(unittest.TestCase):

    # Taking Damage
    def test_take_damage(self) -> None:
        burny: Burnymon = Burnymon("Dave")
        self.assertEqual(burny.get_health(), 15)
        burny.take_damage(5, "dampy")
        self.assertEqual(burny.get_health(), 10)
        
    def test_stringify(self) -> None:
        burny: Burnymon = Burnymon("Dave")
        self.assertEqual("Dave Dave", burny.__str__())
        
if __name__ == '__main__':
    unittest.main()