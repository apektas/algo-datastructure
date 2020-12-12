from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = None
        count = 0
        N = len(flowerbed)
        if n == 0: return True
        for i in range(0, N-1):
            next = flowerbed[i+1]
            if not prev and not next and flowerbed[i]!=1:
                flowerbed[i] = 1
                count+=1
                if count == n: return True

            prev = flowerbed[i]
        if not prev and not flowerbed[N-1]: count+=1
        if count == n: return True
        return False

#print(Solution().canPlaceFlowers([1,0,0,0,1], 2))
#print(Solution().canPlaceFlowers([1,0,0,0,1], 1))
print(Solution().canPlaceFlowers([1,0,0,0,0,1], 2))
print(Solution().canPlaceFlowers([0,0,1,0,1], 1))
print(Solution().canPlaceFlowers([0,0,1,0,0], 2))