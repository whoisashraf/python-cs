# Assume 10 names in a list

list = [["Ada", 50_000], ["James", 40_000],["Mercury", 80_000],["Cain", 30_000],["Sam", 50_000],["Sophie", 65_000],["Mosh", 70_000],["Cree", 60_000],["Madisyn", 60_000],["Trip", 100_000]]

# Split the list into two sub-list namely subList1 and subList2, each containing 5 names. 

subList1 = list[:5] # output: [['Ada', 50000], ['James', 40000], ['Mercury', 80000], ['Cain', 30000], ['Sam', 50000]]
subList2 = list[5:] # output: [['Sophie', 65000], ['Mosh', 70000], ['Cree', 60000], ['Madisyn', 60000], ['Trip', 100000]]

# A new employee (assume the name “Kriti Brown”) joins, and you must add that name in subList2. 

def add_employee(name,salary,sublist):
	sublist.append([name, salary])

add_employee("Kriti Brown", 75_000, subList2)
print(subList2) # output: [['Sophie', 65000], ['Mosh', 70000], ['Cree', 60000], ['Madisyn', 60000], ['Trip', 100000], ['Kriti Brown', 75000]]

# Remove the second employee's name from subList1. 
def remove_employee(number, sublist):
	sublist.pop(number-1)

remove_employee(2, subList1)
print(subList1) # output: [['Ada', 50000], ['Mercury', 80000], ['Cain', 30000], ['Sam', 50000]]

# Merge both the lists. 

merged_list = subList1 + subList2
print(merged_list) # output: [['Ada', 50000], ['Mercury', 80000], ['Cain', 30000], ['Sam', 50000], ['Sophie', 65000], ['Mosh', 70000], ['Cree', 60000], ['Madisyn', 60000], ['Trip', 100000], ['Kriti Brown', 75000]]

# Assume there is another list salaryList.

salaryList = subList1 + subList2
print(salaryList) # output: [['Ada', 50000], ['Mercury', 80000], ['Cain', 30000], ['Sam', 50000], ['Sophie', 65000], ['Mosh', 70000], ['Cree', 60000], ['Madisyn', 60000], ['Trip', 100000], ['Kriti Brown', 75000]]

# Give a rise of 4% to every employee and update the salaryList.  

def raise_salary(list, percentage):
	global salaryList
	new_salary_list = []
	for employee in list:
		new_salary_list.append([employee[0], employee[1] * ((100 + percentage) / 100)])

	salaryList = new_salary_list

raise_salary(salaryList,4)
print(salaryList) # output: [['Ada', 52000.0], ['Mercury', 83200.0], ['Cain', 31200.0], ['Sam', 52000.0], ['Sophie', 67600.0], ['Mosh', 72800.0], ['Cree', 62400.0], ['Madisyn', 62400.0], ['Trip', 104000.0], ['Kriti Brown', 78000.0]]

# Sort the SalaryList and show top 3 salaries. 
salaryList.sort(key = lambda salary: salary[1], reverse = True)
print(salaryList[:3]) # output: [['Trip', 100000], ['Mercury', 80000], ['Kriti Brown', 75000]]


# Design a program such that it converts a sentence into wordlist.  

def to_word_list_reverse(sentence):
	sentence = sentence.split()
	# Reverse the wordlist.
	sentence.reverse()
	print(sentence)

to_word_list_reverse("Design a program such that it converts a sentence into wordlist") # output: ['wordlist', 'into', 'sentence', 'a', 'converts', 'it', 'that', 'such', 'program', 'a', 'Design']

