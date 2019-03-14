"""
@author : CK =>ckrajadurai7@gmail.com
@github : https://github.com/ck2605
@date : 13/03/2019

========================PERFECT NUMBER===========================================
    A number N is said to be perfect Number
        if sum of all its divisors except N is equal to the given Number N...

    For eg:
            6, 28, 496, 8128, 33550336...
            6 is a Perfect Number because
                6 has 1, 2, 3, 6 as its divisors..
                sum of 1 + 2 + 3 = 6..     Hence 6 is a Perfect Number....
"""

n = int(input("enter the no :"))
arr = []
s = 0

for i in range(n+1):
    if i != 0:
        if n % i == 0:
            arr.append(i)

print(arr)
m = arr.__len__()
for i in range(m):
    if arr[i] != n:
        s = s + arr[i]
if s == n:
    print("the number is perfect")
else:
    print("the number is not a perfect number")