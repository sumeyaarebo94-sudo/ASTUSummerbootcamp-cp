class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        j = 0
        ans = 0

        for house in houses:
            while (
                j < len(heaters) - 1
                and abs(heaters[j + 1] - house) <= abs(heaters[j] - house)
            ):
                j += 1

            ans = max(ans, abs(heaters[j] - house))

        return ans