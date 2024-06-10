b = []
while True:
    try:
        a = input()
        b.append(a)

    except EOFError:
        c = {}
        for a in b:
            d = a.upper()
            c[d] = c.get(d, 0) + 1

        sort_c = sorted(c.items())
        for a, count in sort_c:
            print(f"{count} {a}")
        break
