nums=[8,4,0,3,4,0,0,9,0,100,0,25,0,1,6,0]

def move_zeroes(nums):
    # Step1: Initialize non-zero and zeroth element
    nz=0
    z=0
    size=len(nums)

    # If array has 0 or 1 element, nothing to do---> just return that list
    if size<=1:
        return nums 
    
     # Step3:Traverse the array with nz
    while(nz<size):     
        if (nums[nz]!=0):     # If current element is non-zero
            nums[nz],nums[z]=nums[z],nums[nz]
            z+=1            # Move zero pointer forward
        nz+=1        # Always move non-zero pointer forward
    return nums

print(f"After moving zeroes {move_zeroes(nums)}")



