
# Function to count the number of vowels in a string
def count_vowel(arg):
    # Convert parameter to a string and store in a variable
    word = str(arg)
    # Use a variable to keep count of vowels
    count = 0
    # Loop through the string
    for letter in word:
        # Check if string contains a vowel letter
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            # Increment vowel count by one
            count = count + 1
    # Return the result to the caller of the function
    return f"Number of vowels in your name: {count}"

# Function to reverse the order of a string
def reverse(arg):
    # convert parameter to a string and store in a variable
    word = str(arg)
    # Return reversed string to caller of the function
    return word[::-1]

# Function implementing core logic
def main():
    # convert user input to a string and store in a variable
    name = str(input("Your name is: "))
    # convert user input to an integer and store in a variable
    number = int(
        input("Enter the number of characters to display from the left: "))
    # Display requested characters to user
    # Anonymous(lambda) function that returns characters of a string from index 0 till number passed by user
    print(number, "characters from the left: ", (lambda n: name[0:n])(number))
    # Display vowel count to user
    print(count_vowel(name))
    # Display user's name but reversed
    print("Your name reversed: ", reverse(name))

# Call main function to start the prompt
main()
