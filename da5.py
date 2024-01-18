# For each function, describe what it actually does when called with a string argument. If it does not correctly check for lowercase letters, give an example argument that produces incorrect results, and describe why the result is incorrect.

#1

def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True
		else:
			return False

# print(any_lowercase1("amy")) # result : True
# print(any_lowercase1("Amy")) # result : False
# This implementation only checks if the first letter is lower cased


# 2
def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'
          
# print(any_lowercase2("amy")) # result : True
# print(any_lowercase2("Amy")) # result : True
# print(any_lowercase2("AMY")) # result : True
# While we do get True as a result, this function only checks if 'c' is true and does not loop over s at all

 # 3

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# print(any_lowercase3("amy")) # result : True
# print(any_lowercase3("Amy")) # result : True
# print(any_lowercase3("aMY")) # result : False
# This implementation successfully checks for lower cased letters from the beginning of a string but will return false if the last letter in the string is not lower cased, regardless of the string beginning with lower cased letters

# 4

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


# print(any_lowercase4("amy")) # result : True
# print(any_lowercase4("Amy")) # result : True
# print(any_lowercase4("aMY")) # result : True
# print(any_lowercase4("AMY")) # result : False
# print(any_lowercase4("AMy")) # result : True
# print(any_lowercase4("StrInG")) # result : True
# This implementation is correct as it checks if a string contains a lower cased letter. It works by "flagging" lower cased strings which works because it keeps the variable "flag" as a state.


# 5

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# print(any_lowercase5("amy")) # result : True
# print(any_lowercase5("Amy")) # result : False
# print(any_lowercase5("aMY")) # result : False
# print(any_lowercase5("AMy")) # result : False
# print(any_lowercase5("StrInG")) # result : False
# This implementation fails because it only checks if the current letter in the loop is lower cased. 

