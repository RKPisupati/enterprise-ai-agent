from agent.executor import Executor

executor = Executor()

while True:

    question = input("You: ")

    if question == "exit":
        break

    answer = executor.run(question)

    print("Agent:", answer)
