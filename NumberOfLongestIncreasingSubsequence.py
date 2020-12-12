class Solution(object):
    def countLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        #lengths[i] = longest ending in nums[i]
        #count[i] = number of longest ending in nums[i]
        count = [1] * N
        lis = [1]  * N
        for i in range(1, N):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if lis[i] < lis[j]+1:
                        lis[i] = lis[j]+1
                        count[i] = count[j] ## way this is necessary ???
                    elif lis[i] == lis[j]+1:
                        count[i] += count[j]
        maxlength = max(lis)
        print(lis)
        print(count)
        return sum( [count[i] for i in range(len(count)) if lis[i] == maxlength])


print(Solution().countLIS([1,3,5,4,7]))
print(Solution().countLIS([2,2,2,2]))