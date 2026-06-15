class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        total = 0

        for num in nums:
            total += str(num).count(str(digit))

        return total
   