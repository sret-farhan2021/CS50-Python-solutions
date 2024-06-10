def main():
    time = input("What time is it? ")
    convert_time = convert(time)
    output = meal_time(convert_time)
    if output:
        print(output)

def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60

def meal_time(converted_time):
    if 7 <= converted_time <= 8:
        return "breakfast time"
    elif 12 <= converted_time <= 13:
        return "lunch time"
    elif 18 <= converted_time <= 19:
        return "dinner time"
    else:
        return ""

if __name__ == "__main__":
    main()
