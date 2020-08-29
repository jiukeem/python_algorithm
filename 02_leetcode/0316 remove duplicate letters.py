# 내 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        # 알파벳별 횟수 카운트

        stack = []
        for char in s:
            count[char] -= 1
            while stack and stack[-1] > char:
                if count[stack[-1]] > 1:
                    stack.pop()
            stack.append(char)

        return ''.join(stack)







