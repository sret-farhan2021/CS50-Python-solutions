import inflect

def farewell(names):
    if not names:
        return "No names provided."

    p = inflect.engine()
    op = "Adieu, adieu, to " + p.join(names)

    return op

def read_names():
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass
    return names

names = read_names()
print(farewell(names))
