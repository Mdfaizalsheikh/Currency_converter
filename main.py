exchange_rates = {
    "USD": 1.0,
    "EUR": 0.89,
    "JPY": 111.0,
    "GBP": 0.75,
    "AUD": 1.44,
    "CAD": 1.31,
    "CHF": 0.97,
    "CNY": 7.07,
    "SEK": 9.43,
    "NZD": 1.52
}

def convert_currency (amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return None
  
    amount_in_usd = amount/exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount

def main():
    print("Available currencies: USD, EUR, JPY, GBP, AUD, CAD, CHF, CNY, SEK, NZD")
    from_currency = input("Enter the base currency : ") 
    to_currency = input("Enter the target currency : ")
    amount = float(input(f"Enter amount in {from_currency} : "))        
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
       print(f"{amount}{from_currency} is equal to {converted_amount:.2f}{to_currency}")
    else:
        print(" Invalid currency")


if __name__ == "__main__":
    main()

      
