#currey converter

#included a module tpo fetch request from the api
import requests

currencies = [
    ("United States Dollar", "USD"),
    ("Canadian Dollar", "CAD"),
    ("Mexican Peso", "MXN"),
    ("Cuban Peso", "CUP"),
    ("Jamaican Dollar", "JMD"),
    ("Haitian Gourde", "HTG"),
    ("Brazilian Real", "BRL"),
    ("Argentine Peso", "ARS"),
    ("Chilean Peso", "CLP"),
    ("Peruvian Sol", "PEN"),
    ("Colombian Peso", "COP"),
    ("Venezuelan Bolívar", "VEF"),
    ("Euro", "EUR"),
    ("British Pound", "GBP"),
    ("Swiss Franc", "CHF"),
    ("Russian Ruble", "RUB"),
    ("Swedish Krona", "SEK"),
    ("Norwegian Krone", "NOK"),
    ("Danish Krone", "DKK"),
    ("Polish Zloty", "PLN"),
    ("Hungarian Forint", "HUF"),
    ("Czech Koruna", "CZK"),
    ("Bulgarian Lev", "BGN"),
    ("Romanian Leu", "RON"),
    ("Japanese Yen", "JPY"),
    ("Chinese Yuan", "CNY"),
    ("Indian Rupee", "INR"),
    ("South Korean Won", "KRW"),
    ("Singapore Dollar", "SGD"),
    ("Malaysian Ringgit", "MYR"),
    ("Indonesian Rupiah", "IDR"),
    ("Thai Baht", "THB"),
    ("Vietnamese Dong", "VND"),
    ("Philippine Peso", "PHP"),
    ("Pakistani Rupee", "PKR"),
    ("Bangladeshi Taka", "BDT"),
    ("Hong Kong Dollar", "HKD"),
    ("Taiwanese Dollar", "TWD"),
    ("Sri Lankan Rupee", "LKR"),
    ("Nigerian Naira", "NGN"),
    ("South African Rand", "ZAR"),
    ("Egyptian Pound", "EGP"),
    ("Kenyan Shilling", "KES"),
    ("Ghanaian Cedi", "GHS"),
    ("Moroccan Dirham", "MAD"),
    ("Ethiopian Birr", "ETB"),
    ("Tanzanian Shilling", "TZS"),
    ("Ugandan Shilling", "UGX"),
    ("Rwandan Franc", "RWF"),
    ("Zimbabwean Dollar", "ZWL"),
    ("Zambian Kwacha", "ZMW"),
    ("Namibian Dollar", "NAD"),
    ("Australian Dollar", "AUD"),
    ("New Zealand Dollar", "NZD"),
    ("Fijian Dollar", "FJD"),
    ("Papua New Guinean Kina", "PGK"),
    ("Solomon Islands Dollar", "SBD"),
    ("Samoan Tala", "WST")
]

for currency, abbreviation in currencies:
    print(f"{currency} {abbreviation}")

print("------------------------------------------------------------------------")
user_currency = input("Enter the currency abbreviation you would like to convert from---> ").upper()
print("------------------------------------------------------------------------")

print("------------------------------------------------------------------------")
desired_currency = input("Enter the currency abbreviation you want to convert to---> ").upper()
print("------------------------------------------------------------------------")


amount = float(input("Enter the anount of money---> "))

#added frankfurter api for convert the currency
response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={user_currency}&to={desired_currency}")

print("--------------------------------------------------------------------------")
print(f"{amount} {user_currency} is {response.json()["rates"][desired_currency]} {desired_currency}")
print("--------------------------------------------------------------------------")
