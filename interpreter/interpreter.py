input_string = input("Expression: ")
list = input_string.split()
a= int(list[0])
b= int(list[2])
if (list[1]) == "+":
    c= a+b
if (list[1]) == "-":
    c= a-b
if (list[1]) == "*":
    c= a*b
if (list[1]) == "/":
    c= a/b
result = "{:.1f}".format(c)
print(result)
