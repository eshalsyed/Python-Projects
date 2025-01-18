import requests
import json

print("Currency Conversion!")

currencies = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
s = currencies.json()
rates = s["rates"]
print("Here is the list of currencies:\n")
for money in rates:
    print(money)


original = input("What currency would you like to convert from? ")
next = input("What currency would you like to convert to? ")
amount = float(input("Enter amount: "))

if original not in rates and next not in rates:
    print("Invalid currency.")
    exit()


og = rates[original]
ne = rates[next]
calc = (amount/og)*ne

print(f"{amount:.2f}{original} to {next} is {calc:.2f}{next}")
