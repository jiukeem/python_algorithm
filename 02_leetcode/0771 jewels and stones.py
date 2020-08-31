# 내 풀이
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dict = {}
        for char in J:
            dict[char] = 0

        for stone in S:
            if stone in dict.keys():
                dict[stone] += 1

        return sum(dict.values())
# 굿굿 runtime- 상위50프로, memory usage- 상위10프로


# 내 풀이2
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = collections.Counter(S)

        sum = 0
        for char in J:
            if char in counter.keys():
                sum += counter[char]

        return sum
# 방법은 똑같고 counter를 이용해서 코드수를 줄일 수 있음 메모리를 조금 더 쓴다.
# 책의 풀이도 내 것(위의 두개)과 똑같다!! ㅎㅎ기분좋당 맨 마지막 풀이4는 따로 써둔다.


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)
# 리스트 컴프리헨션 대괄호를 넣어서 생각하면 좀 더 이해가 쉽다.
# [s for s in S]는 character를 한 개씩 리스트의 요소로 만든다.
# [s in J for s in S]는 character가 J에 들었는지 불린값으로 요소가 기록된다.
# 그럼 요걸 sum해주면 True는 1로 계산되니까 총 갯수를 세준다! 넘모 똑똑한 방법