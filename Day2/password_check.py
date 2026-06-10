"""
Password Strength Checker: 

 

Take a password as input. Check for length ≥8, uppercase, lowercase, digit, and special character. Show a strength score (Weak / Medium / Strong) with tips to improve. 

Enter password: Hello@123 
--- 
Length: OK Upper: OK Lower: OK 
Digit: OK Special: OK 
Strength: Strong (5/5) 
"Your password is secure!" 
"""

pwd = input("Enter the password: ")
length = False
IsUpper = False
IsLower = False
IsDigit = False
IsSpecial = False
c = 0

if len(pwd) >= 8:
    length = True
    c += 1
    for i in pwd:
        if i.isupper() and IsUpper == False:
            IsUpper = True
            c += 1
        elif i.islower() and IsLower == False:
            IsLower = True
            c += 1
        elif i.isdigit() and IsDigit == False:
            IsDigit = True
            c += 1
        elif i.isalnum() and IsSpecial == False:
            IsSpecial = True
            c += 1
if length == False:
    print("Length should be greater than or equal to 8")
else:
    print("Length: OK")

    print("Upper: OK") if IsUpper else print("Uppercase letter is required")

    print("Lower: OK") if IsLower else print("Lowercase letter is required")

    print("Digit: OK") if IsDigit else print("Digits are required")

    print("Special: OK") if IsSpecial else print("Special charc=acters required")


if c == 5:
    print(f"Strength: Strong ({c}/5)")
    print("Your password is secure!!")
elif c >= 3:
    print(f"Strength: Medium ({c}/5)")
elif c < 3 and c > 0:
    print(f"Strength: Weak ({c}/5)")
