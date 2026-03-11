from research_agent import ResearchAgent
from math_agent import MathAgent


class SupervisorAgent:

    def __init__(self):

        self.research_agent = ResearchAgent()
        self.math_agent = MathAgent()

    def route(self, query):

        if "calculate" in query or any(char.isdigit() for char in query):

            return self.math_agent.run(query)

        else:

            return self.research_agent.run(query)