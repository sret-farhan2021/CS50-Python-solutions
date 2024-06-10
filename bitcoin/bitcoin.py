import sys
import requests
import json


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    rate = float(data["bpi"]["USD"]["rate"].replace(",", ""))
    cost_usd = bitcoins * rate
    print(f"${cost_usd:,.4f}")
except requests.RequestException as e:
    sys.exit(f"Error: Failed to retrieve Bitcoin price from API: {e}")
