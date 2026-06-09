amount = float(input("Enter the amount: "))
people = int(input("Enter number of people: "))
tip = input("Would you like to add tip: y/n: ")
tip_percent = 0
if tip == 'y':
    tip_percent = int(input("Enter tip percentage: "))
sum = amount + (tip_percent/100) * amount
print(f"{(sum/people):.2f}")
