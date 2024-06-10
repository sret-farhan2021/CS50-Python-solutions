import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(AM|PM)$'
    match = re.match(pattern, s)

    if match:
        start_hour, start_minute, start_ap, end_hour, end_minute, end_ap = match.groups()

        if int(start_hour) > 23 or int(start_minute or 0) > 59 or int(end_hour) > 23 or int(end_minute or 0) > 59:
            raise ValueError("Invalid time")

        start_hour = int(start_hour)
        end_hour = int(end_hour)

        if start_hour == 12:
            start_hour = 0
        if end_hour == 12:
            end_hour = 0

        if start_ap == 'PM':
            start_hour += 12
        if end_ap == 'PM':
            end_hour += 12

        return f"{start_hour:02d}:{start_minute or '00'} to {end_hour:02d}:{end_minute or '00'}"
    else:
        raise ValueError("Invalid format")

if __name__ == "__main__":
    main()
