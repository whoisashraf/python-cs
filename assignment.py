# Print welcome message
print("Welcome to the counter game!")
#Convert to integer and store number in a variable
number = int(input("Type a number to count from: "))

#Implement the Count functionality
def count(param):
	#Handle "0" input to avoid an infinite loop
	if param == 0:
		print("Blastoff!")
	#Handle when input > 0
	elif param > 0:
		print(param)
		#Count Down!
		count(param - 1)
	else:
		#Handle when input < 0
		print(param)
		#Count Up!
		count(param + 1)

#Pass number input as a parameter and call count function
count(number)

# when count is 6
# Welcome to the counter game!
# Type a number to count from: 6
# 6
# 5
# 4
# 3
# 2
# 1
# Blastoff!

# when count is -6
# Welcome to the counter game!
# Type a number to count from: -6
# -6
# -5
# -4
# -3
# -2
# -1
# Blastoff!

# when count is 0
# Welcome to the counter game!
# Type a number to count from: 0
# Blastoff!

