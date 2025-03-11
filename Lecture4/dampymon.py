from saalmon import *
class Dampymon(Saalmon):

    def __init__(self, name: str) -> None:
        super().__init__(25, name)
    
    def take_damage(self, dmg: int, type: str) -> int:
        if type == "burny":
            dmg += 5
        return super().take_damage(dmg, type)

'''class Dampymon:

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__health = 25
    
    def take_damage(self, dmg: int, type: str) -> int:
        if type == "burny":
            dmg += 5
        self.__health -= dmg
        return self.__health
    
    def get_health(self):
        return self.__health
    
    def get_name(self):
        return self.__name
    
    def __str__(self) -> str:
        return f"{self.__name} {self.__name}"
'''