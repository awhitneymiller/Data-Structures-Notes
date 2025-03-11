from int_array_list import IntArrayList

test: IntArrayList = IntArrayList()
test.append(2)
test.append(4)
test.append(8)
test.remove_at(1)
print(test.get_at(1)) # 8