def askAndReturnSearchTerm():
    return input("Type a Wikipedia search term: ")

def askAndReturnPrefix():
    prefixes = ['Who is', 'What is', 'The history of']
    for i, prefix in enumerate(prefixes):
        print(f"[{i}] {prefix}")
    selectIndex = input("Select the number of prefix: ")
    return prefixes[int(selectIndex)]

def start():
    content = {}
    content["searchTerm"] = askAndReturnSearchTerm()
    content["prefix"] = askAndReturnPrefix()
    print(content)

start()