class Solution:
    def singleNumber(self,nums:list[int]):
        s={}
        for num in nums:
            s[num]=s.get(num,0)+1

        n =min(s.values())
        key = next((k for k, v in s.items() if v == n), None)
        return key
    
s=Solution()
print(s.singleNumber([2,2,1,1,3]))