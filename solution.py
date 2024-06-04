import requests

def get_rate(from_currency,to_currency,amount):
    fromupper = str(from_currency).upper()
    toupper = str(to_currency).upper()
    resp = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={fromupper}&to={toupper}")
    return resp.json()['rates'][toupper]
