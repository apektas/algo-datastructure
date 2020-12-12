from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        alphabet = defaultdict(int)

        for c in s:
            alphabet[c]+=1

        count = 0
        for i in alphabet:
            if alphabet[i] >= k:
                count+=alphabet[i]

        return count


print(Solution().longestSubstring("aaabb",3))
print(Solution().longestSubstring("ababbc",2))