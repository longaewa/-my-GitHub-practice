# my_module.py

def reverse_text(text):
    """Returns the reverse of the given text"""
    return text[::-1]

def simple_calculator(a, b, operator):
    """
    Performs a basic calculation on two numbers.
    Supported operators: +, -, *, /
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"
