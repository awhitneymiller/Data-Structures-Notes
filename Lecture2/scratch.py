'''
Dynamic vs Static Typing:

Dynamic Typing: variables can holda  value of any type,
and that type can change as the code is being run.

Static Typing: Variables hold a value of a specified type,
and that type cannot be changed while the program is being run.

Type Hints: An optional syntax feature in Python that allows you
to indicate the types of variables, arguments, and returns.
NOTE: This does not affect the way a python file is actually run,
its only used by typecheckers.
x: int = 10
y: str="hello"
def do_something() -> int: (means this returns an int)
    #Some code here, does something
    #returns some value.

run mypy first!!

'''
x: int = 10
y: str="hello"

print(x + y)

def do_something() -> int:
    #Some code here, does something
    #returns some value.
    

x: int = do_something(10, 5)

print(x+x)

