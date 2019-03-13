from array import *
arr = array('i', [])
n = int(input("enter the no of elements:"))
for i in range(n):
    x = int(input("enter the elements:"))
    arr.append(x)
print(arr)
val = int(input("enter the value to search:"))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k = k+1

print(arr.index(val))


