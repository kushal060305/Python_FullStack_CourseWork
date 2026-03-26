#Simple code for add sub mul div
def add(a, b):
    return a + b        
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
# Example usage
num1 = 10   
num2 = 5
print("Addition:", add(num1, num2))
print("Subtraction:", sub(num1, num2))  
print("Multiplication:", mul(num1, num2))
print("Division:", div(num1, num2))