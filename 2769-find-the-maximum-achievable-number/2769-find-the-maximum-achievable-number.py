class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        result = num

        result += t
        result += t

        return result