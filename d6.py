# Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references. 


# An example of python objects with identical objects

name = "Sarah" # a variable whose object has the value "Sarah"

friends_name = "Sarah" # a variable whose object has the value "Sarah"

# print(name is friends_name) # output: True


# An example of python objects with identical values and non-equivalent objects

row_1 = [1,2,3,4,5] # the variable row_1 holds an object with values [1,2,3,4,5]

row_2 = [1,2,3,4,5] # the variable row_2 holds another object with values [1,2,3,4,5]

# print(row_1 is row_2) # output: False

# An example demonstrating the relationship between objects, references, and aliasing

# references

option_1 = [0,2,4,6,8]

option_2 = [1,3,5,7,9]

# the variables option_1 and option_2 reference the objects [0,2,4,6,8] and [1,3,5,7,9] respectively

object_1 = [1,2,3]

object_2 = object_1

# the variable object_1 references the object [1,2,3] which is aliased by the variable object_2.  


"""
A function that takes a list as an argument and returns all even numbers as a list
"""
def filter_even(list):
	# accept a list as an argument 
	# store even numbers
	even = []
	# loop through the numbers
	for i in list:
		# check if the current item in the loop is even
		if i % 2 == 0:
			# append the even number to the even list
			even.append(i)
	# return the result as a list of even numbers
	return even


obj = [1,2,3,4,5,6,7,8,9,10]

print(filter_even(obj))

# The function "filter_even" takes a list as a parameter, appends all even numbers within the list to a variable "even" through the mutation of the "even" variable(i.e the .append() property is destructive). The "list" parameter is a reference to the the object [1,2,3,4,5,6,7,8,9,10] through the argument "obj". The object [1,2,3,4,5,6,7,8,9,10] is aliased by "list" and "obj"



# References 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Green Tea Press. https://greenteapress.com/thinkpython2/thinkpython2.pdf
