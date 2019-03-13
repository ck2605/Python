"""
@author : CK =>ckrajadurai7@gmail.com
@github : https://github.com/ck2605
@date : 13/03/2019


=================================PASCAL TRIANGLE=====================================
if no of row = 5....
ANSWER(o/p):
    1
   212
  32123
 4321234
543212345

"""

n = int(input("enter the no of rows:"))
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(end=" ")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()

