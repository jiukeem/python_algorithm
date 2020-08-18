# 내 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            right = left + 1

            while right < len(nums):
                if nums[left] + nums[right] == target:
                    return [left, right]
                else:
                    right += 1
# 틀리진 않는데 인풋이 길 경우 runtime 에러가 난다. 최악의 경우 모든 경우의 수에 대해서 따져봐서 그러는 듯ㅜㅜ
# left 포인터는 인덱스0부터 포문을 돌리고 right랑 더해보면서 target 값과 다르면 계속 1씩 더해나가는 식
# 아 책설명을 보니 이 방식을 브루트포스라고 한다고 한다. 배열을 두번 반복하면서 모든 조합을 확인하는 방법
# 비효율적인 풀이법의 대명사라고...ㅋㅋㅋㅋ큐ㅠㅠ
# 시간복잡도는 O(n^2)다. (정확히는 n^2/2인데 상수항은 원래 뺀다. 내가 헷갈렸던 이유가 요거네)


# 내 풀이2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            if target - nums[left] in nums:
                return [left, nums.index(target-nums[left])]
# 이 방법은 nums[left] * 2 = target 일 경우 틀린답이 나옴ㅜㅜ
# nums[left]를 nums에서 빼고 진행해볼까 했으나 그러면 index가 앞뒤로 1씩 밀릴테니 안됨


# 책 풀이 - in을 이용한 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return i, nums[i + 1:].index(complement) + (i + 1)
# 내 두번째 풀이와 같은방식이다! 하지만 내가 막힌 부분을 너무 간단히 해결해버렸다
# return 에서 nums.index(complement) 라고 쓰면 if문 사용한 의미가 없이 중복답이 나올 수 있다.
# 그래서 굳이 nums[i + 1:].index(complement) + (i + 1) 라고 쓴다.
# enumerate는 파이썬 내장함수로 인덱스와 값을 한 쌍으로 가져온다.
# 즉, i in range(len(lst)) 하고 lst[i]하면서 쓸거면 range 보다 enumerate 가 훨씬 효율적일 것
# runtime은 상위 75프로로, 효율성이 좋은편은 아니다.
# 책에 따르면 in의 시간복잡도가 O(n)이기 때문에 얘도 전체 시간복잡도가 O(n^2) 지만, 같은 시간복잡도라도 in 이 훨씬 가볍고 빠르다고 한다.
# 그런걸 어떻게 알 수 있지....? 그냥 경험에서 나오는 짬으로 알아야하나요


# 책 풀이2 - 값을 키로, 인덱스를 벨류로 서로 바꿔서 딕셔너리 생성
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        switched = {}
        for i, num in enumerate(nums):
            switched[num] = i

        for i, num in enumerate(nums):
            if target - num in switched and switched[target - num] != i:
                return nums.index(num), switched[target - num]
# 와 어떻게 이런 생각을? 진짜 대단하당..
# 시간복잡도 O(n), runtime 상위 25프로
# 아 근데 nums에 같은 값이 여러개 들어갈 수 있을텐데 그럼 dict로 만드는 과정에서 오류가 생길텐데..?
# 아! 그래서 i 대신 nums.index(num) 을 return 하는 거구나. 같은게 두개면 dict과정에서 첫번째는 덮여버릴거고
# nums.index(num)은 num의 첫번째 인덱스가 살아나니까
# 고단수지만 좀 아슬아슬한걸?



