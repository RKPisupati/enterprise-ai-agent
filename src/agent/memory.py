class Memory:

    def __init__(self):
        self.chat_history = []

    def save(self, question, answer):
        self.chat_history.append({
            "question": question,
            "answer": answer
        })

    def get_history(self):
        return self.chat_history
