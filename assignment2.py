print("A simple division calculator")
print("How it works \n--------------------")
print("numerator / denominator")
#convert input to integer and store in a variable
numerator = int(input("Enter first number: "))

#convert input to integer and store in a variable
denominator = int(input("Enter second number: "))

#introduce runtime error
if denominator == 0:
	print("Error: Division by zero is not allowed as denominator cannot be zero!")
	#create an intentional bug
	print(numerator / denominator)
print(numerator / denominator)


#Significance of Error Handling
# Preventing Crashes: Without error handling, when users enter zero as a denominator, the program would attempt to perform an invalid division operation, leading to a program termination.
# User-Friendly Error Message: The error message provides clear feedback to the user about why the division didn't work as expected. It also instructs them on how to correct the issue.

#Impact of Not Handling the Errors
# Unwanted Termination: The program would crash when attempting to divide by zero, leading to an unexpected program termination.
# Bad User Experience: Encountering a cryptic error message or system error only confuses non technical users.

#The program above fails to recognize that a user input could be 0 which throws an error. Consider validating user input(by comparing if input is 0) and showing a user friendly error message and steps forward. I would instead do:

#refactored code
print("A simple division calculator")
print("How it works \n--------------------")
print("numerator / denominator")
numerator = int(input("Enter first number: "))
denominator = int(input("Enter second number: "))
if denominator == 0:
	print("Division by zero is not allowed, Please enter a non-zero denominator")
else:
	#perform division and store result
	result = numerator / denominator
	print(result)
