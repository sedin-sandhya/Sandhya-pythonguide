s = input("Enter a paragraph: ")
l = s.strip().split(" ")
dict1 = {}
print(l)
for i in l:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
def getVal(item):
    return item[1]
sorted_dict = sorted(dict1.items(), key=getVal, reverse = True)
print(sorted_dict[:5])