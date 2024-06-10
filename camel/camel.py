a = input("camelCase: ")
result = [a[0].lower()]

for char in a[1:]:
    if char.isupper():
        result.extend(['_', char.lower()])
    else:
        result.append(char)

print(''.join(result))
