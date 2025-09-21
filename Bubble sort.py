nums=[8,4,0,3,4,0,0,9,0,100,0,25,0,1,6,0]

def bubble_sort(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

    return nums

print(bubble_sort(nums))