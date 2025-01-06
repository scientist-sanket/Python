class Solution:
    def find_pairs(self,nums:list,k:int)->list:
        pairs=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] ==k:
                    pairs.append((nums[i],nums[j]))

        return pairs
    
s=Solution()
print(s.find_pairs([1,2,3,4],5))