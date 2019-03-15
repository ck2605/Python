"""
@author : CK =>ckrajadurai7@gmail.com
@github : https://github.com/ck2605
@date : 15/03/2019


=================BUBBLE SORT=======================
"Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
if they are in wrong order(Either ascending or descending)."

"""

# bubble sort func for sorting elements in ascending order....
def bubblesort1(arr1):
    n = len(arr1)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr1[j] > arr1[j+1]:
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
    return arr1

# bubble sort func for sorting elements in descending order....
def bubblesort2(arr1):
    n = len(arr1)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr1[j] < arr1[j+1]:
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
    return arr1


arr = []
arr1 = []
n = int(input("enter the limit :"))
for i in range(n):
    e = int(input("enter the element:"))
    arr.append(e)
arr1 = arr
print("the array1 before Bubble sort\n", arr1)
res1 = bubblesort1(arr1)
print("array1 after sort(ascending)\n", res1)
res2 = bubblesort2(arr1)

print("array2 after sort(descending)\n", res2)


