import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too many command-line arguments")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

try:
    with open(input_file) as input:
        reader = csv.DictReader(input)
        with open(output_file, "w") as output:
            header = ["first", "last", "house"]
            writer = csv.DictWriter(output, fieldnames=header)
            writer.writeheader()
            for student in reader:
                last, first = student["name"].split(", ")
                house = student["house"]
                writer.writerow({"first": first, "last": last, "house": house})
except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")
