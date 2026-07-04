from tools.search import search
from tools.calculator import calculate

class Agent:

    def decide(self, question):

        if any(char.isdigit() for char in question):

            return "calculator"

        return "search"

    def execute(self, question):

        tool = self.decide(question)

        if tool == "calculator":

            return calculate(question)

        return search(question)
