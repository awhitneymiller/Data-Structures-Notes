from py_array import PyArray

class IntArrayList:
	def __init__(self) -> None:
		START_SIZE = 8

		self.__items: PyArray = PyArray(int, START_SIZE )
		self.__size: int = 0

	def append(self, to_add: int) -> None: #to_add: this is what is being added to the collection
		self.__check_and_grow()
		self.__items[self.__size] = to_add # Stores 'to_add' at the next available index '__size' in '__items' 
		self.__size += 1 #increments __size since we added to the array

	def get_at(self, index: int) -> int:
		self.__index_validation(index)
		return self.__items[index]

	def remove_at(self, index: int) -> None:
		if index < 0 or index >= self.__size:
			raise ValueError("Requested index out of range.")
		self.__shift_left(index)
		self.__size -= 1

	def insert_at(self, to_add: int, index: int) -> None:
		if index < 0 or index >= self.__size + 1:
			raise ValueError("Requested index out of range.")
		self.__size += 1
		self.__check_and_grow()
		self.__shift_right(index)
		self.__items[index] = to_add



	#Helper Methods
	def __index_validation(self, index: int):
		if index < 0 or index >= self.__size:
			raise ValueError("Requested index out of range")

	def __check_and_grow(self) -> None:
		'''
		Expands the size of self.__items whenever
		it is at capacity
		'''
		#Case 1: Big enough to fit another item,
		#there's no need to grow
		if self.__size < len(self.__items): #seeing if what we have as our max length is less than the actual length of the array
			return            #if it is then no need to expand

		#Case 2: At capacity and need to grow
		#Step 1: Create a new bigger array
		OLD_ARRAY_SIZE = len(self.__items)
		new_items: PyArray = PyArray(int, OLD_ARRAY_SIZE * 2) #makes a new array (new_items) of type PyArray double the size of the old one
		#Step 2: Copy the items from the old array
		for i in range(len(self.__items)):  #going through every index of my old array and assinging it to
			new_items[i] = self.__items[i] # the same index in the new array
		
		self.__items = new_items #take the frame that was holding the old array and point it to the new array!!
	
	def __shift_left(self, index: int) -> None:
		'''
		Shifts all elements to the right of the given index one left
		:param: index Index at which to shift all elements to the right left by 1
		'''
		for i in range(index, self.__size-1):
			self.__items[i] = self.__items[i+1]

	def __shift_right(self, index: int) -> None:
		for i in reversed(range(index, self.__size+1)):
			self.__items[i] = self.__items[i-1]
		
