import sys

if len(sys.argv) > 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith('.py'):
        file1 = sys.argv[1]
    else:
        sys.exit("Not a Python file")
try:
    count = 0
    with open(file1, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                count += 1
    print(f"{count}")

except FileNotFoundError:
    sys.exit("File does not exist")
