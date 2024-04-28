""" 
    Simple Calculator that takes two operand and an operator
"""
def calculator(num1, num2, symbol):
    try:
        # Convert Input parameters to float    
        fNum = float(num1)
        sNum = float(num2)
       
       # Calculator logic
        if symbol == "+":
            return fNum + sNum
        elif symbol == "-":
            return fNum - sNum
        elif symbol == "/":
            return int(fNum / sNum)
        elif symbol == "*":
            return fNum * sNum
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return "Can't divide numbers by zero"
    except:
        # Handle input errors
        return "Please enter a valid number"
       
print("CALCULATOR\nEnter 'exit' to quit\n------------------------------------------------------\n")
# Continously collect user input
while True:
    firstNum = input("Enter first number: ")
    if firstNum == "exit":
        break
    
    symbol = input("Enter mathematical operator: ")
    if symbol == "exit":
        break
    
    secondNum = input("Enter second number: ")
    if secondNum == "exit":
        break
    
    print(calculator(firstNum, secondNum, symbol))