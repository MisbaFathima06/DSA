#1.Brute force solution
nums=[8,4,0,3,4,0,0,9,0,100,0,25,0,1,6,0]

def duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False

print(duplicate(nums))

#HasMap Solution
def contains_duplicate(nums):
    hashSet=set()

    for number in nums:
        if number in hashSet:
            return True
        hashSet.add(number)
    return False
print(contains_duplicate(nums))
