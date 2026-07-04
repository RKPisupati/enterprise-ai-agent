from tools.search import search
from tools.calculator import calculate
class Agent:
    def run(self,q):
        return calculate(q) if any(c.isdigit() for c in q) else search(q)
