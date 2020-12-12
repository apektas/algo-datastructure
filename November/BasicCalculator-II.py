from typing import List
from collections import deque
class Solution:
    #https://leetcode.com/problems/basic-calculator-ii/discuss/658480/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
    def calculate(self, s: str) -> int:
        stack = deque()
        num, sign = 0, '+'
        if not s: return 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = 10*num + int(c)
            if i +1 == len(s) or c in '+-/*':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                sign = c
                num = 0

        # O(n) as we iterate the stack to sum
        return sum(stack)

    def calI(self,expression, index):
        result =0; op ='+'
        while index < len(expression):
            char = expression[index]
            if char in ('+', '-'): op = char
            else:
                if char.isdigit(): value = int(char)
                elif char == '(':
                    value, index = self.calI(expression, index)
        pass


#"3+2*2"
#print(Solution().calculate("3+4*3"))
print(Solution().calculate("-5"))