# Part 1
# import Python's math library
import math

def hypotenuse(x,y):
  """
  Calculates the hypotenuse of a right triangle.

  Arguments:
  x (float or int): The length of the first leg of the triangle.
  y (float or int): The length of the second leg of the triangle.

  Returns:
  result(float or int): The length of the hypotenuse.
  """
  # Check if both x and y are either integers or floats
  if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
    side1 = x
    side2 = y
    # print(side1, side2)
    # Calculate the sum of squares of the two sides
    sum_of_squares = x**2 + y**2
    # print(sum_of_squares)
    # Calculate the square root of the sum_of_squares to find the hypotenuse
    result = math.sqrt(sum_of_squares)
    # print(result)
    # Round the result to 4 decimal places
    result = round(result, 4)
    return result
  # If the input types are not valid, return an error message
  return "Error: All parameters must be numbers (integers or floats)"
  
# Tests
calc = hypotenuse(3,4)
print(calc) # Output: 2.6458
calc = hypotenuse(6,5)
print(calc) # Output: 3.3166
calc = hypotenuse(8,2)
print(calc) # Output: 3.1623
# Status: passed


# Part 2

"""
Creates a calculator class that stores methods to perform mathematical operations
"""
class calculator:
  """
  Adds two integers 

  Arguments:
  x (float or int): The first number.
  y (float or int): The second number.

  Returns:
  result(float or int): The sum of two numbers.
  """
  def add( x, y):
    # Check if both x and y are either integers or floats
    if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
      # Calculate the sum of x and y 
      result = x + y
      # round result to 4 decimal places
      result = round(result, 4)
      # print(result)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
    
  """
  Subtracts two integers

  Arguments:
  x (float or int): The first number.
  y (float or int): The second number.

  Returns:
  result(float or int): The subtraction between two numbers. 
  """
  def subtract( x, y):
    # Check if both x and y are either integers or floats
    if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
      # perform subtraction
      result = x - y
      # round result to 4 decimal places
      result = round(result, 4)
      # print(result)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
  
  """
  multiplies two integers 

  Arguments:
  x (float or int): The first number.
  y (float or int): The second number.

  Returns:
  result(float or int): The multiplication of two numbers.
  """  
  def multiply( x, y):
    # Check if both x and y are either integers or floats
    if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
      # perform multiplication
      result = x * y
      # round result to 4 decimal places
      result = round(result, 4)
      # print(result)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
  
  """
  Divides two integers 

  Arguments:
  x (float or int): The first number.
  y (float or int but not 0): The second number.

  Returns:
  result(float or int): The multiplication of two numbers.
  """  
  def divide( x, y):
    # Check if both x and y are either integers or floats and check if denominator is a not zero 
    if type(x) == int or type(x) == float and type(y) == int or type(y) == float and y != 0:
      # perform division
      result = x / y
      # round result to 4 decimal places
      result = round(result, 4)
      # print(result)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
  
  """
  Sine of a number

  Arguments:
  x (float or int): The angle in degrees.

  Returns:
  result(float or int): The sine of the number. 
  """
  def sin(x):
    # Check if x is are either an integer or a float
    if type(x) == int or type(x) == float:
      # Find the sine
      result = math.sin(x)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
  
  """
  Cosine of a number 

  Arguments:
  x (float or int): The angle in degrees.

  Returns:
  result(float or int): The cosine of the number. 
  """  
  def cos(x):
    # Check if x is are either an integer or a float
    if type(x) == int or type(x) == float:
      # Find the cosine
      result = math.cos(x)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
  
  """
  Tangent of a number 

  Arguments:
  x (float or int): The angle in degrees.

  Returns:
  result(float or int): The tangent of the number. 
  """
  def tan(x):
    # Check if x is are either an integer or a float
    if type(x) == int or type(x) == float:
      # Find the tangent
      result = math.tan(x)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
  
  """
  Square a number 

  Arguments:
  x (float or int): The number to be squared.

  Returns:
  result(float or int): The square of the number.
  """  
  def square(x):
    # Check if x is are either an integer or a float
    if type(x) == int or type(x) == float:
      # square the number
      result = x ** 2
      # round result to 4 decimal places
      result = round(result, 4)
      # print(result)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
  
  """
  Square root of a number

  Arguments:
  x (float or int): The number whose square root is to be calculated.

  Returns:
  result(float or int): The square root of the number. 
  """
  def sqrt(x):
    # Check if x is are either an integer or a float
    if type(x) == int or type(x) == float:
      # find the square root
      result = math.sqrt(x)
      # round result to 4 decimal places
      result = round(result, 4)
      # print(result)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
    
  """
  Raise a number by a power 

  Arguments:
  hx (float or int): The base number.
  y (float or int): The exponent (the power to which x is raised).

  Returns:
  result (float or int): The result of x raised to the power of y.
  """
  def pow(x,y):
    # Check if both x and y are either integers or floats
    if type(x) == int or type(x) == float and type(y) == int or type(y) == float:
      # raise x to the power y
      result = x ** y
      # round result to 4 decimal places
      result = round(result, 4)
      # print(result)
      return result
    # If the input types are not valid, return an error message
    return "Error: All parameters must be numbers (integers or floats)"
    
# initialize the calculator for ease of use
cal = calculator
# Tests for part 2
print(cal.add(1,5.4)) # Output: 6.4
print(cal.subtract(1.4,5)) # Output: -3.6
print(cal.multiply(1,5)) # Output: 5
print(cal.divide(4,2)) # Output: 2.0
print(cal.sin(60)) # Output: -0.3048106211022167
print(cal.cos(90)) # Output: -0.4480736161291701
print(cal.tan(30)) # Output: -6.405331196646276
print(cal.square(5.4)) # Output: 29.16
print(cal.sqrt(49)) # Output: 7.0
print(cal.pow(6,2)) # Output: 36
# Status: passed