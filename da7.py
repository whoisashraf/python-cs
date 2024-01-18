# Looping over multiple Values in a Single Iteration
coordinates = [(1, 2), (3, 4), (5, 6)]

for x, y in coordinates:
    print(f"X: {x}, Y: {y}")

# Parallel Iteration with the zip function
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: Score {score}")

# Loops Over Dictionaries(Key-Value Pairs) with the .items() method
student_grades = {"Alice": 95, "Bob": 88, "Charlie": 92}

for name, grade in student_grades.items():
    print(f"{name}: Grade {grade}")

# Loops Over Dictionaries(Iterating Over Keys or Values) with the .keys() or .values() method
fruit_prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}

for fruit in fruit_prices.keys():
    print(f"Fruit: {fruit}")

for price in fruit_prices.values():
    print(f"Price: ${price}")

# Question

# What are some other cases where tuples can be particularly useful over lists?