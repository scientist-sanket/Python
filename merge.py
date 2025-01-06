class Solution:
    def merge(self,nums1:list[int],m:int,nums2:list[int],n:int)->list:
        nums=[]
        for i in range(len(nums1)):
            if nums1[i]!=0:
                nums.append(nums1[i])
        nums1=[]
        nums1=nums + nums2
        nums1.sort(reverse=False)
        return nums1
    
s=Solution()
print(s.merge([1,2,3,0,0,0],3,[2,4,5],3))