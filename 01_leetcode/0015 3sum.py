# 일단은 브루트포스
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append((nums[i], nums[j], nums[k]))

        return result
# The solution set must not contain duplicate triplets. 조건 만족하게 만드는게 너무 어렵다ㅜㅜ
# 브루트포스조차도 책 보고 겨우겨우 따라했다
# 이 방법은 시간 초과가 뜬다. O(n^3) 이니 당연함
# two sum 과 다르게 인덱스를 보존하지 않아도 된다. 그럴 경우는 sort를 하고 시작하면 편한듯 빅오는 (O(n))일걸


# 두번째 방법은 sort 후 i는 위와 똑같고 나머지 두 개를 투포인터로 사용하는 것
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum == 0 :
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
# runtime 상위 50프로
# '정렬해서 i는 포문으로 돌리고 나머지 두개를 투포인터로' 라는 개념 자체는 짜기 어렵지 않았는데
# 중복처리하는게 끔찍하게 어렵다ㅜㅜ set으로 중복 요소를 지우고 시작할 수 있는 문제도 아니라서.
# 나 혼자였으면 분명히 중복처리에서 헤맸다.

