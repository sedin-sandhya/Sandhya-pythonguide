import random
gval = random.randint(100000, 999999)
print(gval)
count = 3
while(count > 0):
    otp = int(input("Enter the OTP: "))
    if otp != gval:
        count -= 1
        print("You have entered the wrong Otp,",count, " more attempts to go")
    else:
        print("You have entered the valid OTP")
        break
