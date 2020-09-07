class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                res = max(res, sum(nums[i:j]))

        return res
# Status: Time Limit Exceeded
# Algorithm: Brute Force
# Time Complexity: O(n^2)
# Runtime:

