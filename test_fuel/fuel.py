def main():
    while True:
        try:
            fraction = input("Fraction: ")
            result = convert(fraction)
            print(gauge(result))

def convert(fraction):
    a = fraction.split("/")
    numerator = int(a[0])
    denominator = int(a[1])
    if denominator == 0:
        raise ZeroDivisionError("Invalid fraction.")
    elif numerator > denominator:
        raise ValueError("Invalid fraction.")
    else:
        result = (numerator / denominator) * 100
        return round(result)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
