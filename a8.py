

# input.txt's content

# { 

# apple: red 

# banana: yellow 

# cherry: red 

# mango: yellow 

# grapes: black, green 

# } 
 

# Initialize an empty dictionary to store the inverted data

inverted_dict = {}

# Open the input file for reading
with open("input.txt", "r") as file:
	content = ""
	# Read the input file line by line
	for line in file:
		content = content + line
	# Remove curly braces and split the content into a list of lines
	content = content.replace("{", "").replace("}", "").split("\n")
	# Create a cleaned_content list to store non-empty lines
	cleaned_content = []
	# Iterate through the lines to remove empty lines
	for item in content:
		if item.strip():
			cleaned_content.append(item)

	# Update the content to contain only non-empty lines
	content = cleaned_content
	# Process each line to build the inverted dictionary
	for item in content:
		# Split each line at the colon to get keys and values
		pairs = item.split(":")
		# Store the value pair
		values = pairs[0].split(",")
		# Store the key pair
		keys = pairs[1].split(",")
		# Loop over each key
		for key in keys:
			# Loop over each value
			for value in values:
				# Check if the key exists in the inverted dictionary "inverted_dict"
				if key in inverted_dict:
					# Append the new value to the matching key
					inverted_dict[key].append(value)
				# If key doesn't exist in the inverted dictionary "inverted_dict"
				else:
					# Create a new key-value pair in the dictionary and pass the current key,value in the loop
					inverted_dict[key] = [value]
	# Log the inverted dictionary "inverted_dict" for debugging purposes
	# print(inverted_dict) # Output: {' red ': ['apple', 'cherry'], ' yellow ': ['banana', 'mango'], ' black': ['grapes'], ' green ': ['grapes']}
	
# Open the output file for writing
with open("output.txt", "w") as file:
	# Format the inverted dictionary to match required output and write it to the output file "output.txt"
	file.write(str(inverted_dict).replace("{", "{\n\n").replace("}", "\n\n}").replace("'", "").replace("],", "]\n\n").replace("[","").replace("]",""))

# output.txt's content

# {

#  red : apple, cherry

#   yellow : banana, mango

#   black: grapes

#   green : grapes

# }



 # Summary


# The program opens the input file "input.txt" in read mode ("r") using a with statement. This ensures proper file handling.

# The program reads the input file line by line, concatenating each line into the content string variable to read files efficiently.
# The program removes curly braces and split the content into a list of lines for further processing.

# The program creates a cleaned_content list, ensuring that empty lines are excluded by checking if they have any content when stripped of whitespace.

# The program initializes an empty dictionary, inverted_dict, to store the inverted data.

# For each line in the cleaned content, lines get split it at the colon to extract key-value pairs, which are further split into keys and values.

# Using nested loops, inverted_dict is  populated where the keys represent colors and values represent fruits of those colors. If the key exists, the program appends the value to the list of values associated with that key. If the key is not present, a new key-value pair is created.

# The program opens the output file "output.txt" in write mode ("w") and format the inverted_dict to match the required output format by removing any of "[]"or "," found in inverted_dict.

# The formatted data is then written to "output.txt."
