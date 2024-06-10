def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[:2].isalpha():
        return False

    if not (2 <= len(s) <= 6):
        return False

    if s[-1].isdigit() and s[-2].isdigit() and s[-3].isalpha():
        if s[-2] == '0':
            return False

    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False

    if any(char in ['.', ' ', ',', ';', ':', '-', '_'] for char in s):
        return False

    return True

if __name__ == "__main__":
    main()
