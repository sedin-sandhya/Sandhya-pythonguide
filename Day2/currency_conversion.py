"""
    Exchange rate: 1 USD = 84.5000 INR $100.00 USD in all currencies:  
    INR:  ₹84.50  
    EUR:  €87.00    
    GBP:  £75.00   
    JPY:  ¥15,400.00    
    AED:  د.إ367.00    
    CAD:  CA$136.00

    Eg: INR -> GBP
    Step 1: ₹5000 ÷ 84.50  = $59.17 (in USD)  
    Step 2: $59.17 × 0.75  = £44.38 (in GBP)
"""

currencies = {
    "USD" : 1,
    "INR" : 84.50,
    "EUR" : 0.87,
    "GBP" : 0.75,
    "JPY" : 154,
    "AED" : 3.67,
    "CAD" : 1.36
}
def check_currency(currency, currencies):
    if(currency not in currencies.keys()):
        print("The given currency is not supported")
        exit()
        
currency = input("Enter the currency(INR,EUR,GBP,JPY,AED,CAD): ").upper()
check_currency(currency, currencies)
amount = int(input("Enter the amount: "))
target_currency = input("Enter the target currency(INR,EUR,GBP,JPY,AED,CAD): ").upper()
check_currency(target_currency, currencies)

converted_amount = (amount/currencies[currency]) * currencies[target_currency]

print(f"{currency} -> {target_currency}")
print(f"{currency} {amount}")
print(f"{target_currency} {converted_amount:.2f}")
