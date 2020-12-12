from typing import List
from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque(); curNum = 0; curString = ''
        for c in s:
            if c == '[': # if open bracket then append stack
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString




print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
# aaabcbc