def calculator(expression: str):
    try:
        result = eval(expression)
        return f"Result is {result}"
    except Exception as e:
        return f"Error: {str(e)}"