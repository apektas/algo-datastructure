from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
           result.add(''.join([alphabet[ord(w)-ord('a')] for w in word]))

        return len(result)

print(Solution().uniqueMorseRepresentations( ["gin", "zen", "gig", "msg"]))
