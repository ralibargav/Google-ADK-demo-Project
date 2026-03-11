from tools import calculator

class MathAgent:

    def run(self, query):

        expression = query.replace("calculate", "").strip()

        result = calculator(expression)

        return f"MathAgent Result: {result}"