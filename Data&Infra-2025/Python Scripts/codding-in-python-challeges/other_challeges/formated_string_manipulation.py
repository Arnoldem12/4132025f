#Basic String Manipulation
#Write a function called greet that takes two arguments: name (a string) and age (an integer). 
#The function should return a string message in the format "Hello, [name]! You are [age] years old."


def greet(name, age):
    #return "Hello, " + name + "! You are " + str(age) + " years old."
    return f"Hello, {name}! You are {age} years old."

# Output: Hello, Alice! You are 30 years old.
print(greet("Alice", 30)) 

