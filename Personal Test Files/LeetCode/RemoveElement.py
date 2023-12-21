def removeElement(nums, val):
    nums1 = nums[:]
    for i in nums1:
        if i == val:
            nums.remove(i)
    print(nums)
    return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))