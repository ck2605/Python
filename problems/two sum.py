"""
@author : CK =>ckrajadurai7@gmail.com
@github : https://github.com/ck2605
@date : 13/03/2019


=================================TWO SUM=============================================================================
    Given an array of integers and a target value..
    find the two numbers whose sum is equal to the given target...
    GIVEN:
        arr = [1, 4, 10, 13] , target = 17
    ANSWER:
        result =  [2, 4]   ==> 2 and 4 are the positions of 4 and 13...
"""

res = []
arr = [1, 4, 10, 13]
target = 17
flag = 0
n = arr.__len__()
for i in range(n):
    if flag == 0:
        for j in range(n):
            if (arr[i] + arr[j]) == target:
                # print(arr[i], arr[j])
                res.append(i+1)
                res.append(j+1)
                flag = 1
                break

if flag == 1:
    print("result = ", res)
else:
    print("no match found")
