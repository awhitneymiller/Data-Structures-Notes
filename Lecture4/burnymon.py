from saalmon import *
class Burnymon(Saalmon):

    def __init__(self, name: str) -> None:
        super().__init__(15, name)


'''class Burnymon:
    Burnymon singe their opponents with the fire of 5 suns.
    - Start with 15 health
    - Deal burny damage
    
    def __init__ (self, name:str):
        self._name: str = name
        self._health: int = 15
        
    def take_damage(self, dmg:int, type:str) -> int:
        self._health -= dmg
        return self._health
    
    def get_health(self):
        return self._health
    
    def get_name(self):
        return self._name
        
    def __str__(self) -> str:
        return f"{self._name}: {self._health}" #f adds spaces instead of + ""
'''

not_charizard: Burnymon = Burnymon("Dave")
# print(not_charizard.health)
# not_charizard.take_damage(5, "dampy")
# print(not_charizard.health)
#not_charizard._health -= 5

#print(not_charizard.health) - another way other than the get methods
print(not_charizard.get_health())
print(not_charizard)