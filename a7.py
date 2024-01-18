input_data = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}


def invert_list(list):
    # Initialize an empty inverted dictionary
    inverted_dict = {}
    for student, courses in list.items():
        # Iterate through the list of courses for each student
        for course in courses:
            # Check if the course is not already a key in the inverted dictionary
            if course not in inverted_dict:
                # Add the course and student into the inverted dictionary
                inverted_dict[course] = [student]
            else:
                # Add additional student to the inverted dictionary
                inverted_dict[course].append(student)
    return inverted_dict
    


# Print the inverted dictionary
print(invert_list(input_data)) # Output: {'CS1101': ['Stud1'], 'CS2402': ['Stud1', 'Stud2'], 'CS2001': ['Stud1', 'Stud2'], 'CS1102': ['Stud2']}

