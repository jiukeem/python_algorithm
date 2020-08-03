# 슬라이싱 사용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
# 슬라이싱은 내부적으로 굉장히 빠르게 동작한다고 함. 속도를 따질 때 좋은 선택
# reverse(), 혹은 reversed() + join() 보다 다섯배이상 빠르고 포문보다는 열배이상


# 리스트로 변환 방식 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for char in s:
            if char.isalnum():
                lst.append(char.lower())
                # isalnum 함수는 영문자, 숫자 여부를 판별해줌.
                # 위에서 정규식으로 돌린걸 하나씩 점검해주고 있는 것

        while len(lst) > 1:
            if lst.pop(0) != lst.pop()
            # pop은 해당 요소를 return 하면서 동시에 리스트에서 삭제해버리기 때문에
            # 인덱싱해서 비교 + 그 요소를 삭제 를 따로 구현할 필요없이 한번에 가능하다.
                return False

        return True
        # 리스트가 빈 경우 바로 True로 return
# 문자열을 리스트로 맵핑하고 있는데 데이터 구조를 다루는 측면에선 좋지만
# 연산 과정에서 시간소모가 크다. 지금도 포문을 써서 일일히 확인하고 있음


# 데크 자료형을 이용하는 방법도 있는데 데크를 내가 아직 안배웠으니 그건 나중에~