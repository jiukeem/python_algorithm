class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def gen_combi(nums, case, count, k):
            if count == k:
                self.res.append(case)
            else:
                for i, num in enumerate(nums):
                    gen_combi(nums[i + 1:], case + [num], count + 1, k)
            return

        self.res = []
        nums = [i + 1 for i in range(n)]
        gen_combi(nums, [], 0, k)
        return self.res
# Status: Accepted
# Algorithm: Recursion
# Time Complexity: O(n!)
# Runtime: 600ms (top 56.5%)
# Intuition: 46번 순열문제와 똑같은 방식



