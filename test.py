# Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.
def print_out(param):
    print(param)
    
print_out("Ashraf")
#The argument for the above function is "Ashraf" and the parameter for the function is the "param" on function declaration

#Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which. 

print_out("Hannah") #takes a value as an argument

name = "Hannah"
print_out(name) #takes a variable as an argument

print_out(16 * 2) #takes an expression as an argument

#Construct a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.
def local():
    age = 32
    print(age)
    
local()
print(age)# error because the variable is locally scoped to the function declaration

#Construct a function that takes an argument. Give the function parameter a unique name. Show what happens when you try to use that parameter name outside the function. Explain the results.
def unique(special):
    print("special")
    
print(special)# results in an error as the parameter "special" isn't available outside of the function

#Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.
unsafe = "constant"
def global_mutation():
    unsafe = "global"
    print(unsafe)
    
global_mutation()#mutates the original unsafe variable because the declaration is  globally scoped

Anyone have ideas on how I could make code explanations better? Are these technically explained enough? 
