def heap(arr,a,b):
    large = b
    left = 2*b+1
    right = 2*b+2

    if left < a and arr[b] < arr[left]:
        large = left

    if right < a and arr[large] < arr[right]:
        large = right

    if large != b:
        arr[b], arr[large] = arr[large], arr[b]
        heap(arr,a,large)

def heapsort(arr):
    a = len(arr)
    for b in range(a//2,-1,-1):
        heap(arr,a,b)

    for b in range(a-1,0,-1):
        arr[b],arr[0] = arr[0],arr[b]
        heap(arr,b,0)

arr = []
c = int(input("Enter number of elements you want to sort : "))
for d in range(0,c):
    e = int(input())
    arr.append(e)

print("Initial format is : ",arr)

heapsort(arr)
a = len(arr)
print("Sorted format is : ")
for b in range(a):
    print("%d" % arr[b], end=' ')