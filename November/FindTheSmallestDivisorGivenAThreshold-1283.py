import math
class Solution(object):
    def smallestDivisior(self, nums, threshold):
        compute_sum = lambda x: sum([math.ceil(n/x) for n in nums])

        # search boundaries for the divisor
        left, right = 1, 2

        # search boundaries for the divisor
        while compute_sum(right) > threshold:
            left = right
            right <<= 1 ## multiply by 2

        # binary search
        while left<=right:
            pivot = (right + left) >> 1
            num = compute_sum(pivot)
            if num > threshold:
                left = pivot + 1
            else:
                right = pivot - 1

        # at the end of loop, left > right,
        # compute_sum(right) > threshold
        # compute_sum(left) <= threshold
        # --> return left
        return left

print(Solution().smallestDivisior([1,2,5,9], 6))

# very good resource!!!
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/777019/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.




