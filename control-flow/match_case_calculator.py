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
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = first number / second number
        print(f"The result is {result}.")
else:
    print("Not a valid operation")
