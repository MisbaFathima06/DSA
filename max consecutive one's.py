nums=[0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1]

def consecutive_ones(nums):
    maxCount=0
    count=0
    for i in range(len(nums)):
        if nums[i]==0:
            count=0
        else:
            count+=1
        maxCount=max(count,maxCount)
    return maxCount

print(consecutive_ones(nums))