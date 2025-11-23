def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform an arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): One of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result of the operation, or a message for invalid division.
    """

    if operation == 'add':
        return num1 + num2

    elif operation == 'subtract':
        return num1 - num2

    elif operation == 'multiply':
        return num1 * num2

    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2

    else:
        return "Error: Invalid operation."
