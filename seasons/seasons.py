from datetime import date
import sys
import inflect

def main():
    user_date = input("Date of Birth: ")
    try:
        user_date = date.fromisoformat(user_date)
    except ValueError:
        sys.exit("Invalid date")

    age_in_mins = calculate_age_in_mins(user_date)

    p = inflect.engine()
    age_words = p.number_to_words(age_in_mins, andword='')
    print(f"{age_words.capitalize()} minutes")

def calculate_age_in_mins(user_date):
    current_date = date.today()

    difference = current_date - user_date

    difference_in_mins = difference.total_seconds() / 60

    return int(difference_in_mins)

if __name__ == "__main__":
    main()
