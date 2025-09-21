nums=[8,4,3,4,9,100,100,25,0,0, 1,6]

def second_smallest(nums):
    if len(nums)<2:
        return None     ## Not enough elements to find 2nd small no
    
     # Step1: Initialize first two numbers
    if nums[0]<nums[1]:
        max1,max2=nums[0], nums[1]
    else:
        max1,max2=nums[1],nums[0] 
  
   # Traverse from 2nd index 
    for i in range(2,len(nums)):
        if nums[i]<max1:
            max2=max1
            max1=nums[i]
        elif nums[i]<max2 and nums[i]!=max1:
            max2=nums[i]
    
    return max2     #we want only 2nd larsmallestgest element

print(f"The second smallest element is: {second_smallest(nums)}")
            
            