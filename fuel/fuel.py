while True:
    try:
        fract = input("Fraction: ")
        a = fract.split("/")
        numerator = int(a[0])
        denominator = int(a[1])
        if denominator == 0:
            print("Error: Invalid fraction.")
        elif(numerator > denominator):
            print("Error: Invalid fraction.")
        else:
            result = (numerator / denominator) * 100

            if result >= 99:
                print("F")
            elif result <= 1:
                print("E")
            else:
                print(f"{result:.0f}%")

            # Break out of the loop if successful
            break

    except ValueError:
        print("Error: Please enter a valid numerical fraction.")
    except ZeroDivisionError:
        print("Error: Invalid fraction.")
    except Exception as e:
        print(f"Error: {e}")
