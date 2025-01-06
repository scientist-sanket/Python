def majorityElement(nums):
    count={}
    n=len(nums)
    for num in nums:
        count[num]=count.get(num,0)+1

        if count[num] > n/2:
            return num
    


nums=[1,1,2,2,2,1,1]
print(majorityElement(nums))

