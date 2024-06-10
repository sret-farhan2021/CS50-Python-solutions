a = input("Input: ")
result = ""
for char in a:
    if char in ["a","e","i","o","u","A","E","I","O","U"]:
        continue
    else:
        result += char
print(result)
