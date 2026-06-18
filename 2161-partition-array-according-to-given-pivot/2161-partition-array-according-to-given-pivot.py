class Solution:
    def pivotArray(self, nums, pivot):
        n = len(nums)
        result = [0] * n

        left = 0

        for num in nums:
            if num < pivot:
                result[left] = num
                left += 1

        right = n - 1

        for i in range(n - 1, -1, -1):
            if nums[i] > pivot:
                result[right] = nums[i]
                right -= 1

        while left <= right:
            result[left] = pivot
            left += 1

        return result