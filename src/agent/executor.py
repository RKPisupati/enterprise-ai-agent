from agent.agent import Agent
from agent.memory import Memory
class Executor:
    def __init__(self): self.a=Agent(); self.m=Memory()
    def run(self,q):
        ans=self.a.run(q); self.m.save(q,ans); return ans
