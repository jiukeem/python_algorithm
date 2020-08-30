# 내 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        # 알파벳별 횟수 카운트

        stack = []
        for char in s:
            count[char] -= 1
            if stack and char < stack[-1]:
                while stack and count[stack[-1]] > 0:
                    stack.pop()

            stack.append(char)

        return ''.join(stack)
# 내가 한 건 여기까지가 한계인데 해결하지 못하는 케이스들이 있다ㅜㅜ
# 이미 해당 char이 stack에 잘 담겨있는 경우인데 그 조건을 코드 어디다가 넣어야하는지 감을 못잡는 것 같다.


# 책 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)

        stack = []
        for char in s:
            counter[char] -= 1
            if char in stack:
            # 내가 놓친 부분
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return ''.join(stack)
# 그냥 가장 먼저 char in stack을 체크해주면 되는구나. stack 안에서의 위치와는 상관없이
# 코드를 제대로 짰다면 이미 잘 되어 있으리라고 추측하고 그냥 저렇게 간단히 확인해주는 과정을 추가하면 된다.
# 그리고 나는 내 머리속의 논리를 그대로 옮겨서 if 문 안에 while문이 들어가 있는데
# 그것도 while 문으로 합쳐서 한줄로 줄일 수 있다.
# 꼭 stack을 써야한다는 조건은 없지만 만약 스택을 활용해서 하고 싶다면
# 사실 char in stack은 올바르지 않다. 스택이라는 추상자료형의 기능에는 탐색연산이 없기 때문
# 꼭 스택을 정석대로 쓰고 싶다!하면 stack과는 별개로 seen이라는 세트를 하나 만들어서 해결할 수 있다.
# 아직 부족하지만 혼자서 짠 것도 어느정도 솔루션의 흐름을 쫓아가고 있는 것 같아 기분이 좋다.ㅎㅎ


# 책 풀이 - 정석 stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)

        stack = []
        seen = set()
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)





