from burnymon import *
from dampymon import *
from saalmon import *
import unittest

not_charizard: Burnymon = Burnymon("Dave")
not_charizard.take_damage(5, "dampy")
print(not_charizard.get_health())

sudsturtle: Dampymon = Dampymon("Sudsy")
sudsturtle.take_damage(5, "burny")

# [!] Should print 15 b/c our Dampymon started 
# with 25 health and took 5 base damage and
# 5 bonus burny damage
print(sudsturtle.get_health())