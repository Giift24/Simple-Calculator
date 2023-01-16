import math

def calculator():
  # Get the user input
  num1 = input("Enter a number (or a letter to exit): ")
  if num1.isdigit():
    num1 = float(num1)
    # Get the operator
    op = input("Enter an operator: ")
    # Get the second number
    num2 = float(input("Enter another number: "))

    # Perform the calculation
    if op == "+":
      result = num1 + num2
    elif op == "-":
      result = num1 - num2
    elif op == "*":
      result = num1 * num2
    elif op == "/":
      result = num1 / num2
    elif op == "**":
      result = num1 ** num2
    elif op == "sqrt":
      result = math.sqrt(num1)
    elif op == "sin":
      result = math.sin(num1)
    elif op == "cos":
      result = math.cos(num1)
    elif op == "tan":
      result = math.tan(num1)
    elif op == "log":
      result = math.log(num1)
    elif op == "ln":
      result = math.log(num1, math.e)
    else:
      result = "Invalid operator"

    # Print the result
    print(result)

# Continuously run the calculator
while True:
  calculator()
