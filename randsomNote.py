from _collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        dictionary = defaultdict(int)
        for i in range(0, len(magazine)):
            dictionary[magazine[i]] += 1

        for i in range(0, len(ransomNote)):
            if(ransomNote[i] not in dictionary): return False
            dictionary[ransomNote[i]] -= 1
            if(dictionary[ransomNote[i]] < 0): return False

        return True

print(Solution().canConstruct("daa","aaa"))


