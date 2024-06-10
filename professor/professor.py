import random

def main():
    level = get_level()
    problems = generate_problems(level)
    score = solve_problems(problems)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input())
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def generate_problems(level):
    problems = []
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problems.append((x, y))
    return problems


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


def solve_problems(problems):
    score = 0
    for x, y in problems:
        correct_answer = x + y
        tries = 0
        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        else:
            print(f" {x} + {y} = {correct_answer})")
    return score


if __name__ == "__main__":
    main()
