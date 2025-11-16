<<<<<<< HEAD
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation selected.")
=======
first number = float(input("Enter the first number: "))
 second number= float(input("Enter the second number: "))
operation =input("Choose the operation (+, -, *, /): ")
if operation == "+":
    result = first number + second number
    print(f"The result is {result}.")
elif operation =="-":
    result = first number - second number
    print(f"The result is {result}.")
elif operation =="*":
    result = first number * second number
    print(f"The result is {result}.")
elif operation =="/":
    if second number == 0:
        print("Cannot divide by zero")
    else:
        result = first number / second number
        print(f"The result is {result}.")
else:
    print("Not a valid operation")
>>>>>>> f867acfdb39ec601bccaebba94be267bb9e4b15d
