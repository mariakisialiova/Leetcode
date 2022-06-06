import math

class Solution:
    def rangeBitwiseAnd(self, a: int, b: int) -> int:
        shiftcount=0
    
        while(a!=b and a>0):
            shiftcount=shiftcount+1
            a=a>>1
            b=b>>1
         
        return a<<shiftcount
