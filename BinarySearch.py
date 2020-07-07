a = []
b = int(input("Enter the number of element in list : "))
for c in range(0,b):
    d = int(input())
    a.append(d)

print("Initial format is : ",a)
a.sort()
print("Sorted format is :",a)

first = 0
last = len(a) - 1
status = False

s = int(input("Enter the number to search : "))
while (first <= last and not status):
    middle = (first + last) // 2
    if(a[middle] == s):
        status = True
    elif(s <= a[middle]):
        last = middle - 1
    else:
        first = middle + 1

if(status == True):
    print("The value %d present in position %d"%(s,middle+1))
else:
    print("Value not found")