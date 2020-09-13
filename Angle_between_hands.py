# https://leetcode.com/problems/angle-between-hands-of-a-clock/


class Solution:
    def angleClock(self, hour, minutes):
        H = {
            12: 0,
            1: 5,
            2: 10,
            3: 15,
            4: 20,
            5: 25,
            6: 30,
            7: 35,
            8: 40,
            9: 45,
            10: 50,
            11: 55
        }
        min_angle = (360 / 60) * minutes
        hour_angle = ((360 / 60) * (H[hour] + ((1 / 12) * minutes)))
        ans = abs(min_angle - hour_angle)
        if ans > 180:
            ans = 360 - ans
        return ans


S = Solution()
print(S.angleClock(12, 30))
