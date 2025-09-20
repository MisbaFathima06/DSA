nums=[8,4,0,3,4,0,0,9,0,100,0,25,0,1,6,0]
nums.sort()
key=int(input("Enter the key: "))

def binary_search(nums,key):
    #Step1: Initialize low and high
    low=0
    high=len(nums)-1


    while(low<=high):
       
        mid=(low+high)//2       # we need only integer value as mid

        # Case 1: Key found at mid
        if key==nums[mid]:
            return mid
        
        # Case 2: Key is smaller → search left half
        if key<nums[mid]:
            high=mid-1
            low=low

        # Case 3: Key is larger → search right half
        if key>nums[mid]:
            low=mid+1
            high=high
    
    return -1       #key not found

print("Sorted array:", nums)
print("Key found at index:", binary_search(nums, key))

        