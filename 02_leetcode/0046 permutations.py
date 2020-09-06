class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def gen_perm(nums, case):
            if len(nums) == 0:
                self.res.append(case)
            else:
                for i, num in enumerate(nums):
                    gen_perm(nums[:i] + nums[i+1:], case + [num])
            return

        self.res = []
        gen_perm(nums, [])
        return self.res
# Status: Accepted
# Algorithm: Recursion
# Time Complexity: O(n!)
# Runtime: 36ms (top 7.6%)
# Intuition: 재귀를 써야겠다는 건 보자마자 생각했는데 구현이 생각보다 어려웠다.
#            기존 nums에 변형을 가자면서 하니 첫 포문에서 끝이 나버렸다. 
#            저런 애들은 원본은 그냥 놔두고 인덱싱 등으로 파라미터를 조정해주자
#            근데 이거 시간복잡도가 n! 인데 왜 이렇게 runtime이 짧지? 최선의 방법이 이거라서 그런건가