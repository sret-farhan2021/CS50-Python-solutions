user_greeting = input("Greeting: ").strip().lower()  # Ignore leading whitespace and make it lowercase
if user_greeting.startswith("hello"):
        print("$0")
elif user_greeting.startswith("h"):
        print("$20")
else:
        print("$100")
