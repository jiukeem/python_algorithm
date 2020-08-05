# 내 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = sum([x for x in nums[::2]])

        return result
# runtime 상위 10퍼센트~~ 근데 list를 한번 더 만들기 때문에 공간복잡도는 좋지않다.
# 리스트 없이 포문으로 해보자
# 아! sum(nums[::2]) 로 하면 될 것을 괜히 한번 꼬아 생각했다.
# 책을 보면 아예 한줄로 코드를 짤 수도 있다. return sum(sorted(nums)[::2])


# 내 풀이2
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for i in range(0, len(nums), 2):
            result += nums[i]

        return result
# 시간복잡도는 살짝 안좋아지고 대신 공간복잡도가 조금 개선됨

