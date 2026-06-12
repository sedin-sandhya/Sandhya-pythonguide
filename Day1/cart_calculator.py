dict = {"soap": 70, "toothbrush": 60, "trimmer": 1200, "juice": 50, "mirror": 1000, "shoe stand": 900}
list = []
print("Available Items: ")
print("Items   Price")
for i in dict:
    print(i, "-", dict[i])
True
while(True):
    i = input("Enter Item name :")
    a = input("Do u want to continue(y/n): ")
    list.append(i)
    if(a != 'y'):
        break
tot = 0
for i in list:
    if i in dict:
        tot += dict[i]
        print(i , "-", dict[i])
print("Item Total: ", tot)
if tot > 1000: 
    print("Discount Applied: ", tot/10)
    tot = tot - (tot/10)
   
print("Total Amount: ", tot)


