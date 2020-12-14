'''
How does above recursive relation work?
There are n – 1 ways for element 0 (this explains multiplication with n – 1).
Let 0 be placed at index i. There are now two possibilities, depending on whether or not element i is placed at 0 in return.
1. i is placed at 0: This case is equivalent to solving the problem for n-2 elements as two elements have just swapped their positions.
2. i is not placed at 0: This case is equivalent to solving the problem for n-1 elements as now there are n-1 elements, n-1 positions and every element has n-2 choices

So it's going to be the same thing as D(n - 2)
# fn(n) = (n-1) * (fn(n-2) + fn(n-2)
'''


from functools import lru_cache
cache = dict()

''' Top-down approach with memoization'''
def countDerangements(n):
    if n == 1: return 0
    if n == 2: return 1
    return  (n-1)*(countDerangements(n-2) + countDerangements(n-1))

def countDerangementsWithMemoization(n):
    if n == 1: return 0
    if n == 2: return 1
    if n in cache: return cache[n]
    cache[n] = (n-1)*(countDerangements(n-2) + countDerangements(n-1))
    return cache[n]


def countDerangementsWithMemoization(n):
    if n == 1: return 0
    if n == 2: return 1
    if n in cache: return cache[n]
    cache[n] = (n-1)*(countDerangements(n-2) + countDerangements(n-1))
    return cache[n]

@lru_cache(None)
def countDerangementsWithLRUCache(n):
    if n == 1: return 0
    if n == 2: return 1
    if n in cache: return cache[n]
    cache[n] = (n-1)*(countDerangements(n-2) + countDerangements(n-1))
    return cache[n]

print(countDerangements(4))
print(countDerangements(3))

# for i in range(1, 60):
#     print(" When N={} derangement count={}".format(i, countDerangements(i)))

# for i in range(1, 60):
#     print(" When N={} derangement count={}".format(i, countDerangementsWithMemoization(i)))

## again raised # of recursive function call limit exception
# for i in range(1, 60):
#     print(" When N={} derangement count={}".format(i, countDerangementsWithLRUCache(i)))


# Bottom-up approach
## O(n) space
def countDerangementBottomUp(n):
    dp = [0]*(n+1)
    dp[1], dp[2] = 0 , 1
    for i in range(3,n+1):
        dp[i] = (i-1)*(dp[i-1]+dp[i-2])
    return dp[n]

# constant space
def countDerangementBottomUpWithConstantSpace(n):
    prevPrev = 0; prev = 1
    for i in range(3,n+1):
        next = (i-1)*(prevPrev + prev)
        prevPrev, prev = prev, next
    return prev


print(countDerangementBottomUp(40))
print(countDerangementBottomUp(3))


print(countDerangementBottomUpWithConstantSpace(40))
print(countDerangementBottomUpWithConstantSpace(3))




