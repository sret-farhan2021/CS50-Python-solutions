def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    return True

if __name__ == "__main__":
    main()
