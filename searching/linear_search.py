# Searching Algorithm
# LINEAR SEARCH
# given an array of elements not in the ordered manner,search a given KEY is present or not....
a = list()                                                   # define a variable as list(array)
flag = 0                                                     # declaring flag value to '0'
n = int(input("enter the no of elements"))                   # Getting limit(array length) from user..
for i in range(n):
    m = int(input("enter the element"))
    a.append(m)                                              # appending each element to the array 'a'
print(a)
key = int(input("enter the search key :"))                   # Getting the search key from the user..
for i in range(n):                                           # searching for the element
    if a[i] == key:
        flag = 1
        j = i
        break
if flag == 1:
    print("the element is found at position ", j+1)          # printing the result...
else:
    print("the element is not found")

