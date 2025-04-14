# Check Balanced Parentheses
# Create a function called is_balanced_parentheses that takes a string containing only parentheses, 
# brackets, and curly braces as input and returns True if the parentheses are balanced and False otherwise. 
# The parentheses are considered balanced if they are closed in the correct order. 
# Your function should use only built-in Python tools.

def is_balanced_parentheses(string):
    stack = []
    for char in string:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack