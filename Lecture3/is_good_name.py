MAX_LEN: int = 16
MIN_LEN: int = 4

def is_good_name(var_name: str) -> bool: #takes in a string, outputs a boolean
	if len(var_name) == 0:
		raise ValueError('var_name may not be empty')
	if(MIN_LEN <= len(var_name) <= MAX_LEN and var_name[0].islower()):
		return True
	return False
	
# Good variable names
print(is_good_name("test"))
print(is_good_name("good_var"))
	
# Bad variable names
print(is_good_name("o"))
print(is_good_name("really_explanatory_variable_name"))
print(is_good_name("LOUD_VAR"))