import math

class Solution:
    def myPow(self,x:float,n:int)-> float:
        result=math.pow(x,n)
        return result
    
s=Solution()
print(s.myPow(2.1,3))