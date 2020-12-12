
# time: O(n),  space: O(n)
def twoSum(nums, target):
    values = dict()
    for i in range(len(nums)):
        if (target - nums[i]) in values : return ( values[target-nums[i]], i)
        values[nums[i]] = i
    return (-1,-1)

print(twoSum([2,7,11,15], 9))

x, y =5