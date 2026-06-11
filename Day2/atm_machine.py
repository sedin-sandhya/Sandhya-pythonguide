"""ATM Machine:  

Simulate a basic ATM. User enters a PIN (3 attempts max). On success, show balance and let them withdraw/deposit. Block the card after 3 wrong PINs. 

Welcome to PyBank ATM 
Enter PIN: **** 
> Balance: ₹12,500.00 
> 1. Withdraw 2. Deposit 3. Exit 
Enter choice: 1 
Enter amount: 2000 
> Withdrawn ₹2,000. New balance: ₹10,500.00 """


import random
pin = 7483
print("pin: ", pin)
count = 3
balance = random.randint(10000, 9000000)

while(count > 0):
    pin_input = int(input("Enter the pin: "))
    if pin == pin_input:
        print("Balance: Rs", balance)
        break
    else:
        count -= 1
        if(count == 0):
            print("No more attempts to go")
            break
        print(count, "more attempts to go")

if pin == pin_input:
    while(True):
        print("1. Withdraw 2. Deposit 3. Exit")
        option = int(input("Enter your choice: "))
        if option == 1:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Sufficient balance not available")
            else:
                balance -= amount
                print("Withdrawn: Rs", amount, "New balance: Rs", balance)
        elif option == 2:
            deposit = int(input("Enter amount to be deposited: "))  
            balance += deposit
            print("Deposited Amount: Rs", deposit, "New balance: Rs", balance)
        elif option == 3:
            exit()     
        else:
            print("Enter a valid choice")
        choice = input("Do you want to Continue(y/n): ")
        if choice == 'n':
            break



