# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """


n=121
d=""

for i in  (len(str(n)),0,-1):
    d=str(d)+((n[i]))
print(d)         
if d==str(n):
    
    print("palindrome")
else:
    print("not")
           

