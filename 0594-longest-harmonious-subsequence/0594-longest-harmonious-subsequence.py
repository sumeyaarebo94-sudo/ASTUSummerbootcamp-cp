class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        maxLHS = 0

        for key in freq:
            if key + 1 in freq:
                currLHS = freq[key] + freq[key + 1]
                maxLHS = max(maxLHS, currLHS)

        return maxLHS   