def main():
    text = input("Input: ")
    output = value(text)
    print(f"Output: {output}")

def value(greeting):
    user_greeting = greeting.strip().lower()
    if user_greeting.startswith("hello"):
            return 0
    elif user_greeting.startswith("h"):
            return 20
    else:
            return 100

if __name__ == "__main__":
    main()
