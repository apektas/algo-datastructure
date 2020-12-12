import math
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.calculateVal(n)
        fast = self.calculateVal(n)
        while (fast != 1 and self.calculateVal(fast) != 1):
            slow = self.calculateVal(slow)
            fast = self.calculateVal(self.calculateVal(fast))
            # if(fast == 1): return True
            if (fast == slow and fast != 1): return False
        return True


    def calculateVal(self, n):
        result = 0;
        while n // 10:
            result += math.pow(n % 10, 2)
            n = n // 10

        if (n): result += math.pow(n, 2)
        return result

print(Solution().isHappy(1))