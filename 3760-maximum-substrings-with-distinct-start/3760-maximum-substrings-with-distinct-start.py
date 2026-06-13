class Solution:
    def maxDistinct(self, s: str) -> int:
        chars = set()

        for ch in s:
            chars.add(ch)

        return len(chars)
        