"""
@author : CK =>ckrajadurai7@gmail.com
@github : https://github.com/ck2605
@date : 13/03/2019

==============================STAIRCASE(#) PATTERN=====================================================================
IF ROW = 5
ANSWER(O/P):
# 
# # 
# # # 
# # # # 
# # # # # 
"""

n = int(input("enter the row limit:"))
for i in range(n+1):
    for j in range(i):
        print("# ", end="")
    print()
    
