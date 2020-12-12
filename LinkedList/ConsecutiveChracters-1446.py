class Solution(object):
    def maxPower(self, s):
        if not s: return 0
        result = 0
        slow = 0
        for fast in range(len(s)):
            if s[slow] == s[fast]:
                result = max(result,fast-slow+1)
            else:
                slow = fast
        return result

print(Solution().maxPower("a"))