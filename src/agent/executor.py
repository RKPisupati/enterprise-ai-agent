from agent.agent import Agent
from agent.memory import Memory

class Executor:

    def __init__(self):

        self.agent = Agent()

        self.memory = Memory()

    def run(self, question):

        answer = self.agent.execute(question)

        self.memory.save(question, answer)

        return answer
