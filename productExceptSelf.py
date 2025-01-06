class Solution:
    def productExceptSelf(self,nums:list[int])-> list[int]:
        n=len(nums)
        result=[1] * n

        left_product=1
        for i in range(n):
            result[i]=left_product
            left_product *=nums[i]

        right_product=1
        for i in range(n-1,-1,-1):
            result[i] *= right_product
            right_product *=nums[i]
        return result

s=Solution()
print(s.productExceptSelf([1,2,3,4]))