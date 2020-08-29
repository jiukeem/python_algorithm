# 내 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '[': ']', '{': '}'}
        if not s:
            return True

        if len(s) %2 != 0:
            return False

        middle = len(s) // 2
        lst1 = []
        lst2 = []

        for i in range(middle):
            lst1.append(s[i])
            lst2.append(s[i+middle])

        lst1.reverse()
        while lst1 and lst2:
            if dict[lst1.pop()] != lst2.pop():
                return False

        return True
# 풀이 자체가 틀렸다 ()[] 같이 구성되어 있으면 처리하지 못한다(false로 return한다)
# 결국 이렇게 쉬운 풀이로는 할 수 없고 stack 자료구조를 사용해야 한다.


# 다시 한 번 도전!
# 내 풀이2
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')': '(', ']': '[', '}': '{'}
        # 짝꿍들 만들어줬다

        stack = []
        for str in s:
            if str not in dict:
                stack.append(str)
                # 여는 괄호(items)들을 stack에 추가해준다.

            if str in dict and not stack:
                return False
                # 닫는 괄호를 만났는데 stack이 비어있을 경우 False 출력
            elif str in dict and dict[str] != stack.pop():
                return False
                # stack이 비어있지 않더라도 stack의 가장 마지막 요소와 매치가 안되면 False 출력

        return not stack
# 우와아아아아아 혼자 헤맨 끝에 해냈다!
# runtime 상위 15프로, memory usage 상위 5프로! 너무 좋다
# 책 풀이도 거의 유사하다. append(push)와 pop이 O(1) 이기 때문에
# 리스트는 스택을 구현하기에 아주 좋다
# 내가 dict라고 이름붙인 저 딕셔너리를 보통 table이라고 이름 붙이는 듯 하다.
# 아 내가 if/ elif 로 처리한 저 부분을 위의 if와 합하여 좀 더 간결하게 처리할 수 있다.


# 책 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        # 테이블은 보기 편하게 이런식으로 줄바꿈을 해준다.

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
            # 위의 if에 대한 elif로 처리하면 char in table 을 생략할 수 있다
                return False

        return not stack
# 더 간결하고 이해하기 쉽다. 시간/공간복잡도는 당연히 같다


# 0830 복습 겸 다시한번
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 리스트로 구현한 스택 추상자료형을 사용하자
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in table.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != table[char]:
                    return False

        return not stack
# 옛날보다 성장했군... 










