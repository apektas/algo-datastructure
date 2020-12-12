from collections import deque
class Solution(object):
    ## if some other parantesis includes in string
    def isValid(self, s):
        dictonary = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        reverseDict = { v: k for k,v in dictonary.items()}
        stack = deque()

        for i in s:
            if len(stack)!=0 and i in reverseDict and stack[-1] ==reverseDict[i]:
                stack.pop()
            elif i in dictonary:
                stack.append(i) ## needs this value to be in

        return len(stack) == 0


print(Solution().isValid("{bb[aa]}"))
