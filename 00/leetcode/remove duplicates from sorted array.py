class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

# 네시간걸림..ㅋㅋㅋㅋㅋㅋㅋ 알고리즘이 이런거구나
# 시간,공간복잡도와 in-place, two-pointer 등을 공부했음
# 메모리 distribution은 상위권, 근데 runtime은 하위25프로다
# 릿코드 엄청 좋당


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        a = 0
        while a < (len(nums) - 1):
            if nums[a] == nums[a + 1]:
                del nums[a + 1]
            else:
                a += 1
        return len(nums)
    
# del 을 쓰면 runtime이 줄어들고 메모리가 늘어난다. 
# 근데 del을 써도 in-place sorting 을 만족하는건가? 이거 공부 좀 해야겠다