def safe_divide(numerator, denominator):
    try:
        # Attempt numeric conversion
        num = float(numerator)
        den = float(denominator)

        # Attempt division (might raise ZeroDivisionError)
        result = num / den
        return f"The result is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Both inputs must be numeric."
