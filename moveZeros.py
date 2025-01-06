class Solution:
    def moveZeroes(self, nums: list[int]) -> list:
        count=0
        lst=[]
        for i in nums:
            if i==0:
                count+=1
            if i!=0:
                lst.append(i)
        for i in range(count):
            lst.append(0)
        for i in range(len(nums)):
            nums[i]=lst[i]
        return nums

s=Solution()
print(s.moveZeroes([0,1,0,3,12]))