def safe_divide(numerator, denominator):

    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt to perform the division
        result = num / den

        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Catch the specific error for division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Catch the specific error for non-numeric input
        return "Error: Please enter numeric values only."