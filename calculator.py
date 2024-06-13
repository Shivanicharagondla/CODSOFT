def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    operand1 = int(input("Enter the first operand: "))
    operand2 = int(input("Enter the second operand: "))
    operator = input("Enter an operator (+, -, *, /): ")
    
    if operator == '+':
        result = add(operand1, operand2)
    elif operator == '-':
        result = subtract(operand1, operand2)
    elif operator == '*':
        result = multiply(operand1, operand2)
    elif operator == '/':
        result = divide(operand1, operand2)
    else:
        result = "Invalid operator!"
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()
