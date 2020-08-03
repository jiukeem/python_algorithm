# 투포인터 사용
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        right = len(s) - 1
        for left in range(len(s)//2):
            s[left], s[right] = s[right], s[left]
            right -= 1
# 책에 나와있는 방법은 위의 것인데 나는 왠지 while 문을 별로 안좋아하는 듯 하다.
# 오류가 날 때까지 기다리는 느낌이랄까.. 시스템이 불안정한 느낌
# 그래서 포문으로도 한번 짜보았다. 잘 돌아간다ㅎㅎ
# 걸리는 시간은 212ms로 동일하다.


# 짱짱인 파이썬 기본 함수를 쓰는 방법
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
# 문자열에는 슬라이싱이 있다면 리스트에는 reverse!
# 새로운 변수를 만들어내지 않고 s를 변경한다. a = s.reverse() 랑 다르게
# 앗 리스트도 슬라이싱이 된다고 한다. 근데 플랫폼에 따라 제대로 작동하지 않을 수도 있다고 하니 이건 생각하지 말자
# 리버스함수는 200ms