total = 0
due = 50
while total < 50:
    amt = int(input("Insert Coin: "))
    if amt == 25 or amt == 10 or amt == 5:
        total += amt
        due = 50 - total
        print("Amount Due:", due)
    else:
        print("Amount Due:", due)
owed = total - 50
print("Change Owed:", owed)
