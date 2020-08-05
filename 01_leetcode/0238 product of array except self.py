# 내 풀이
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            product = 1
            for ele in nums[:i] + nums[i+1:]:
                product *= ele
            result.append(product)

        return result

# 문제에서 내건 조건은 division 을 사용하지 말고, O(n) 에 해결하라는 것
# 전체곱구한뒤 포문 돌리면서 나누는 방식은 아웃, 내가 한 포문 두번도 타임아웃ㅜㅜ
# 선택사항으로 constant space complexity 도 있다. (아웃풋 제외)

# 책 풀이
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        result = []

        # i의 왼쪽값들을 곱한 리스트
        for i in range(len(nums)-1):
            left.append(nums[i] * left[-1])

        # i의 오른쪽값들을 곱한 리스트
        for i in range(len(nums)-1, 0, -1):
            right.append(nums[i] * right[-1])

        # 두 리스트를 곱해줌(right는 인덱스 거꾸로)
        for i in range(len(nums)):
            result.append(left[i] * right[len(nums)-i-1])

        return result
# wow 이 아이디어 누가 처음 생각해내신거죠?? 말도안됨 너무 똑똑해
# 정확히 말하면 책의 코드와는 조금 다르다. 책의 해설을 읽고 그 아이디어로 내가 짠 코드로,
# output 값 말고도 left와 right 리스트가 있기 때문에 공간복잡도가 O(n)이다.
# output 리스트를 계속해서 업데이트 해나갈 수 있으면 공간복잡도(1)을 만족할 수 있다. 한번 해보자


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        # 똑같이 i의 왼쪽값들을 곱한 리스트지만 여기에 바로 업데이트 작업을 해줄거임
        for i in range(len(nums)-1):
            output.append(nums[i] * output[-1])

        # right는 리스트없이 바로 더할거라서 곱한 값을 계속 업데이트하면서 지니고 가는 vairable이 필요
        right_product = 1
        for i in range(len(nums)-1, 0, -1):
            right_product *= nums[i]
            output[i-1] *= right_product

        return output
# 시간복잡도, 공간복잡도 모두 개선됐다.