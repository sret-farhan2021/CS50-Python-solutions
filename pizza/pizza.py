import sys
from tabulate import tabulate
import csv

if len(sys.argv) > 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith('.csv'):
        file1 = sys.argv[1]
    else:
        sys.exit("Not a CSV file")
try:
    with open(file1, 'r') as file:
        csv_reader = csv.reader(file)
        table = list(csv_reader)
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
