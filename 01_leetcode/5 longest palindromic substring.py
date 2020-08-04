# 내 답안
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palinedromes = []

        # 왼쪽 포인터는 0부터 끝까지
        for left in range(len(s)):
            # 오른쪽 포인터는 맨끝부터 앞으로
            right = len(s) - 1

            # 두개의 포인터 slice가 펠린드롬인지 판별하고 맞으면 리스트에 추가
            # 틀리면 right 한칸씩 앞으로 당기면서 체크
            while left <= right:
                slice = s[left: right]
                if slice == slice[::-1]:
                    palinedromes.append(slice)
                else:
                    right -= 1

        return palinedromes.sort()[-1]
# 메모리 부족이라고 뜸ㅠㅠ
# 책에서는 슬라이딩 윈도우, 다이나믹 프로그래밍, LCS 등을 사용하고 있는데 아직 안배웠으므로 나중에 다시 풀어보자

