def calculate(expression):

    try:
        return eval(expression)

    except Exception:
        return "Invalid expression"
