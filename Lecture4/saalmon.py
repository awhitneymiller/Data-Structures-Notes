from abc import *

class Saalmon(ABC):
    
    def __init__(self, health: int, name: str) -> None:
    #the -> None in a function definition is a type hint indicating that the function does not return a value.
        self.__health = health
        self.__name = name
    
    def take_damage(self, dmg: int, type: str) -> int:
        #The stuff in parentheses is the parameter list for the function. 
        # It defines what arguments the function expects when called.
        #self: Refers to the instance of the class (used in instance methods).
        #dmg: int: Means the function expects an argument named dmg that should be an integer.
        #type: str: Means the function expects an argument named type that should be a string.
        #-> int: This is a return type hint, meaning the function is expected to return an integer.
        self.__health -= dmg
        return self.__health
    
    def __str__(self) -> str:
        return f'{self.__name} {self.__name}'
        #The f' in Python is used to create f-strings (formatted string literals).
        # It allows you to embed variables and expressions directly into a string using curly braces
        
    def get_health(self) -> int:
        return self.__health
    #getter function!!
    
    def get_name(self) -> int:
        return self.__name