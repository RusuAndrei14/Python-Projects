"""
/////First Try/////
import freecurrencyapi.client
from requests import get
from pprint import PrettyPrinter
import freecurrencyapi

INITIAL_URL = "https://app.freecurrencyapi.com"
API_KEY = "fca_live_YFsHAoqR847kwPU91MOHnml5e5VsZGenUMM5NC8x"
client = freecurrencyapi.client('API_KEY')

printer = PrettyPrinter()

def show_currencies():
    endpoint = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
    data = get(endpoint).json()
     
    data = list(data.items())
    data.sort()
    printer.pprint(data)
    return data 

def print_currencies(currencies):
    for name, currency in currencies:
        name = client.currencies = ['EUR', 'CAD']
        code = currency['code']
        symbol = currency.get('symbol', "") 

        print(f'{name} - {code} - {symbol}')
        print(symbol)
data = show_currencies()
print_currencies (data)
"""
import requests

INITIAL_URL = "https://api.freecurrencyapi.com/v1/latest"
CURRENCY_URL = "https://api.freecurrencyapi.com/v1/currencies"
API_KEY = "fca_live_YFsHAoqR847kwPU91MOHnml5e5VsZGenUMM5NC8x"


def exchange_amount():
    
    full_url = f"{INITIAL_URL}?apikey={API_KEY}&base_currency={from_currency}&currencies={to_currency}"

    response = requests.get(full_url)
    data = response.json()

    rate = data["data"][to_currency]

    convert_amount = amount * rate
    return convert_amount

def show_currency():

    full_currency_url = f"{CURRENCY_URL}?apikey={API_KEY}"

    response = requests.get(full_currency_url)
    data = response.json()

    for code, info in data["data"].items():

        name = info.get("name", "Unknown")
        symbol = info.get("symbol", "")
        print(f'{code} - {name} {symbol}')

while True:
    print("\nList - Listing the Currencies")
    print("Convert - Converts from 1 Currency to another")
    mode = input("Choose: (q to quit): ").capitalize()

    if mode == "Q":
        print("Goodbye!")
        break
    elif mode == "List":
        show_currency()
    elif mode == "Convert":
        from_currency = input('What is the first currency? (3-letter Code): ').upper()
        amount = float(input("What is the amount? "))
        to_currency = input("What is the currency you want to convert to? ").upper()
        rate = exchange_amount()
        print(f"{amount} {from_currency} = {round(rate, 2)} {to_currency}")
    else:
        print("Invalid option.")



