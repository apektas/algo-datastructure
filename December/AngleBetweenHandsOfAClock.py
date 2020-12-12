class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # note that all should have same unit - minute based!!!
        hourAngle = (360/(12*60)) * (hour*60+minutes)
        minAngle = 360/60*minutes
        angle = abs(hourAngle - minAngle)
        return min(angle, 360-angle)


print(Solution().angleClock(3,00)) # 90