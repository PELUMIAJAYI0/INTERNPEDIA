#currey converter

import requests

user_currency = input("Enter the cirrency you would like to convert from---> ").upper()

desired_currency = input("Enter the currency you want to convert to---> ").upper()


amount = float(input("Enter the anount of money---> "))
response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={user_currency}&to={desired_currency}")

print(f"{amount} {user_currency} is {response.json()["rates"][desired_currency]} {desired_currency}")
