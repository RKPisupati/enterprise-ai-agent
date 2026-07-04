knowledge = {

"Pega":"Pega is a low-code platform.",

"Python":"Python is a programming language.",

"AI":"Artificial Intelligence enables machines to reason."
}

def search(query):

    for key in knowledge:

        if key.lower() in query.lower():
            return knowledge[key]

    return "No information found."
