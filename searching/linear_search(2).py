# Searching Algorithm
# LINEAR SEARCH
# given an array of elements not in the ordered manner,search a given KEY is present or not....
from array import *                                          # importing array func from lib
arr = array('i', [])                                         # declaring an array
flag = 0
n = int(input("enter the no of elements:"))                  # Getting array length from the user
for i in range(n):
    x = int(input("enter the elements:"))                    #Getting the elements from the user
    arr.append(x)
print(arr)
val = int(input("enter the value to search:"))
for e in arr:
    if e == val:
        flag = 1
        break
if flag == 1:   
    print("the element is found at :",arr.index(val))         # printing the position of the element 
else:
    print("the elements is not found")

