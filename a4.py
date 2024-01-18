# According to Downey, A. (2015), potential reasons for function failures include incorrect function arguments, improperly implemented function logic, and incorrect return values.

# Functions can fail when arguments received are not of the expected type.
# For example a function that takes two numbers and adds them.
def add_v1(x,y):
	"""
	Add two integers 
	"""
	# post condition
	return x+y

print(add_v1("9",8)) # Output: Error
# This may seem weird to a user, not everyone knows that strings and integers aren't the same.

#We might want to fix this by checking the type for the input
def add_v2(x,y):
	"""
	Add two integers 
	"""
	# precondition
	if type(x) == int and type(y) == int:
		# post condition
		return x+y
	# post condition
	return 'Please use integers only! \nIntegers are 1, 2, 3 and not "1", "2", etc'

print(add_v2("8",6))  # Output: Please use integers only! Integers are 1, 2, 3 and not "1", "2", etc
print(add_v2(7,4)) # Output: 11



# Functions can also fail when we write instructions that are logically false.
# Let's take at the add_v2 function again. While I was writing the function logic, I did
def old_add_v2(x,y):
	"""
	Add two integers together
	"""
	if type(x) and type(y) == int:
		# post condition
		return x+y
	# post condition
	return 'Please use integers only! \nIntegers are 1, 2, 3 and not "1", "2", etc'

#print(old_add_v2("8",6))  # Output: Error?!
# At first I was puzzled. It might be obvious to you but not to me at the time. 
# The logical error here is "type(x)", it returns true but I thought that I had checked the type of "x" and "y" but doing "type(x) and type(y) == int"
# "type(x) == int and type(y) == int" ended up being equivalent to I intended to implement

# Functions can also fail when we return the wrong value.
# Let's look at an example
class old_calculator:
	"""
	Houses methods to implement calculations
	"""
	err_message = 'Please use integers only! \nIntegers are 1, 2, 3 and not "1", "2", etc'

	def add(self,x,y):
		"""
		Add two integers
		"""
		# precondition
		if type(x) == int and type(y) == int:
			result = x + y
			# post condition
			return result
		# post condition
		return self.err_message

	def subtract(self,x,y):
		"""
		Subtract two integers
		"""
		# precondition
		if type(x) == int and type(y) == int:
			result = x - y
			# post condition
			return self.err_message
		# post condition
		return self.err_message

calculator = old_calculator()
print(calculator.subtract(4,5)) # Please use integers only! Integers are 1, 2, 3 and not "1", "2", etc
# The result here isn't what we expected. That's because immediately after "result = x - y" I wrote "return self.err_message" instead of "return result"
# Here's the corrected version of our calculator
class calculator:
	"""
	Houses methods to implement calculations
	"""
	err_message = 'Please use integers only! \nIntegers are 1, 2, 3 and not "1", "2", etc'

	def add(self,x,y):
		"""
		Add two integers
		"""
		# precondition
		if type(x) == int and type(y) == int:
			result = x + y
			# post condition
			return result
		# post condition
		return self.err_message

	def subtract(self,x,y):
		"""
		Subtract two integers
		"""
		# precondition
		if type(x) == int and type(y) == int:
			result = x - y
			# post condition
			return result
		# post condition
		return self.err_message

calculator = calculator()
print(calculator.subtract(4,5)) # Output: -1


# My question to everyone is "Knowing that temporary variables are advised when writing programs, how often do you use them? Most of the time, I end up wrapping what I want to debug in print(). Won't this the achieve the same goal or is there something I'm missing?"

# References 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Green Tea Press.  https://greenteapress.com/thinkpython2/thinkpython2.pdf