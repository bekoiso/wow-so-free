"""import requests
import pandas as pd

def get_rate(from_currency, to_currency, amount):
    fromupper = str(from_currency).upper()
    toupper = str(to_currency).upper()
    resp = requests.get(f"https://api.exchangerate-api.com/v4/latest/USD?amount={amount}&from={fromupper}&to={toupper}")
    return resp.json()['rates'][toupper]

df = pd.read_csv('survey_results_public.csv')

currency = str(df.loc[14, 'Currency'][:3])

comp_total = str(df.loc[14, 'CompTotal'])

print(get_rate(currency,'USD',comp_total))"""

import requests
import pandas as pd
df = pd.read_csv('survey_results_public.csv')

def get_exchange_rate(from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    data = response.json()
    if 'rates' in data and to_currency in data['rates']:
        return data['rates'][to_currency]
    else:
        return None

def convert_currency(from_currency, to_currency, amount):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

# 사용자로부터 입력 받기
from_currency = str(df.loc[17469, 'Currency'][:3])
to_currency = 'USD'
amount = str(df.loc[17469, 'CompTotal'])

# 환율 계산
result = convert_currency(from_currency, to_currency, amount)
if result is not None:
    print(f"{from_currency}에서 {to_currency}로 변환한 금액은 {result:.2f} {to_currency} 입니다.")
else:
    print("환율을 가져오는 데 문제가 발생했습니다.")
