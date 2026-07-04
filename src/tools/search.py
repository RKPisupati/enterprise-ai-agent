KB={"pega":"Pega is a low-code platform."}
def search(q):
    return KB.get("pega") if "pega" in q.lower() else "No information found."
