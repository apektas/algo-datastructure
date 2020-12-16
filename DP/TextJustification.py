'''
The function below calculates the “badness” of the justification result,
giving that each line’s capacity is w:
calcBadness = (line) => line.length <= w ? pow(w — line.length, 2) : Number.MAX_VALUE;
Why diff²? Because there are more punishments for “an empty line with a full line” than “two half-filled lines.”
Also, if a line overflows, we treat it as infinite bad.
'''

##  What’re the subproblems?
# For every positive number i smaller than len(words),
# if we treat words[i] as the starting word of a new line, what’s the minimal badness score?

'''
How to solve the subproblems?
The total badness score for words which index bigger or equal to i is 
calcBadness(the-line-start-at-words[i]) + the-total-badness-score-of-the-next-lines. 

We can make different choices about what words contained in a line, and choose the best one as the solution to the subproblem.
# https://medium.com/@davidguandev/introduction-to-dynamic-programming-with-examples-bc04dca3ccee
'''

# start at the end
# formatting last element of the array

## Isabel sat on the step
##   1     2  3   4   5
# format(index): if the word[index] is at the beginning of the line
# line width = 10
# f(4) = (10-len(word[4]))^2 = 36 - it is the last element so there is no other way to arrange

# f(3) = case 1 -> 3 and 4 at the same line = cost: 4
#        case 2 -> 3 and 4 at different line: 49 + f(4)

# f(2) = min (inf or 16 + f(4) or 64 + f(3) )

class Solution:

    def __init__(self, words, lineLength):
        self.words = words
        self.lineLength = lineLength

    def badnessScore(self, txtLength):
        if txtLength >= self.lineLength: return float('inf')
        return pow(self.lineLength-txtLength,2)

    # for loop exclusive: meaning toIndex is not counted
    def countChars(self, fromIndex, toIndex):
        totalChars = 0
        for i in range(fromIndex, toIndex):
            totalChars += len(self.words[i])
            # do not add extra space for last one
            if i < toIndex-1:
                totalChars +=1
        return totalChars

    def formatTxt(self, index):
        if index == len(self.words): return 0

        score = float('inf')
        for x in range(index+1, len(self.words)+1):
            curTextLength = self.countChars(index, x)
            curScore = self.badnessScore(curTextLength) + self.formatTxt(x)
            score = min(score, curScore)

        return score

    def formatTxtMemoization(self, index, cache):
        if index == len(self.words): return 0
        if index in cache: return cache[index]

        score = float('inf')
        for x in range(index+1, len(self.words)+1):
            curTextLength = self.countChars(index, x)
            curScore = self.badnessScore(curTextLength) + self.formatTxtMemoization(x, cache)
            score = min(score, curScore)
            cache[index] = score
        return score

    def formatBottomUpApproach(self):
        scores = [0]*(len(self.words)+1)
        # pointers to store links
        pointers = [0] * len(self.words)

        # startPos, endingPos (this is exclusive), step
        for i in range(len(self.words)-1, -1, -1):
            score = float('inf')
            for j in range(i+1, len(self.words)+1):
                curScore = self.badnessScore(self.countChars(i, j)) + scores[j]
                if curScore < score:
                    score = curScore
                    pointers[i] = j
            scores[i] = score

        self.printText(pointers)
        return scores[0]

    def printText(self, pointers):
        index = 0
        while index < len(pointers):
            line = self.words[index:pointers[index]] # last one exclusive
            print(" ".join(line))
            index = pointers[index]


print(Solution("Isabel sat on the step".split(), 10).formatTxt(0))
print(Solution("Isabel sat on the step".split(), 10).formatBottomUpApproach())
# print(Solution("The total badness score for words which index bigger or equal to i is The total badness score for words which index bigger or equal to i is ".split(), 10).formatTxt(0))
print(Solution("The total badness score for words which index bigger or equal to i is The total badness score for words which index bigger or equal to i is ".split(), 40).formatTxtMemoization(0, dict()))
print(Solution("The total badness score for words which index bigger or equal to i is The total badness score for words which index bigger or equal to i is ".split(), 40).formatBottomUpApproach())


