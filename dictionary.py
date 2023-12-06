monthCoversion = {
  "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

month = input("enter in short month name")
print(monthCoversion[month])

## currency 

currency_rates = {
    "USA": 1,
    "CAN": 1.3,
    "EUR": 0.85,
    "GBP": 0.72,
    "JPY": 113.23,
    "AUD": 1.36,
    "INR": 74.83,
    "CNY": 6.44,
    "BRL": 5.35,
    "ZAR": 15.19,
    "RUB": 73.29,
    "MXN": 20.13,
    "KRW": 1187.47,
    "TRY": 11.42,
    "IDR": 14288.71,
    "NGN": 411.33,
    "EGP": 15.68,
    "SAU": 3.75,
    "ARG": 99.74,
    "NZD": 1.46
}

amount = float(input("enter amount "))
rate = input("enter currency ")

print("$ " + currency_rates[rate] * amount )