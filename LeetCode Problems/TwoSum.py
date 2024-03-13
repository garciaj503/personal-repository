def twoSum(nums, target):
    l = len(nums)
    for i in range(l - 1):
        for j in range(i + 1, l):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def twoSum2(nums, target):
    l = len(nums)
    count = 0
    for i in range(1, l):
        if nums[count] + nums[i] == target:
            print([count, i])
            break
        else:
            count += 1
            
numeros = [1,2,3,4,5,6,7,8,9]
targetero = 17
twoSum2(numeros, targetero)