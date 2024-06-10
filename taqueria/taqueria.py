a= {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total=0
while True:
    try:
        b = input("Item: ")
        b = b.title()
        if b in a:
            total = total + a[b]
            print("Total: ${:.2f}".format(total))
        else:
            print("Invalid item.")

    except EOFError:
        print("Error")
        break
