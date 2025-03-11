from typing import Any, Union

class PyArray:
    def __init__(self, arr_type: type, argument: Union[list, int]) -> None:
        self.__length: int = 0
        self.__elements: list = []
        self.__arr_type: type = arr_type
        if(isinstance(argument, int)):
            self.__length = argument
            for i in range(self.__length):
                self.__elements.append(None)
        elif(isinstance(argument, list)):
            for item in argument:
                if not isinstance(item, self.__arr_type):
                    raise ValueError(f"Incompatible types: All values in argument must be of type {self.__arr_type}. Recieved type {type(item)} instead.")
            self.__elements = argument.copy() 
            self.__length = len(argument)
        else:
            raise ValueError(f"Incompatible types: All argument must be of type {list} or {int}. Recieved {type(argument)} insttead.")

    def __str__(self) -> str:
        return str(self.__elements)
    
    def __getitem__(self, key: Union[slice, int]) -> Any:
        if(isinstance(key, slice)):
            start, stop, step = key.indices(self.__length)
            return PyArray(self.__arr_type, [self.__elements[i] for i in range(start, stop, step)])
        elif(isinstance(key, int)):
            return self.__elements[key]
        else:
            raise ValueError(f"Incompatible types: key must be of type  {type(int)} or {type(slice)}. Recieved type {type(key)} instead.")
    
    def __setitem__(self, key: int, new_value: Any) -> None:
        if isinstance(new_value, self.__arr_type) or new_value is None:
            self.__elements[key] = new_value  
        else: 
            raise ValueError(f"Incompatible types: new_value must be of type {self.__arr_type}. Recieved {type(new_value)} instead.")
    
    def __len__(self) -> int:
        return self.__length