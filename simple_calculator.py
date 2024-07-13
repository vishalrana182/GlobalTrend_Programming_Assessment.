def calculator():
    num1 = float(input("first int: "))
    num2 = float(input("2nd int: "))
    operator = input("Enter the operator: ")

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2


result = calculator()
print(f"Result: {result}")
