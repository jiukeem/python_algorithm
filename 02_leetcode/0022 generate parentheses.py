# my solution
import copy

class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        count = {")": 0, "(": 0}
        self.recursion(n, count, "")
        return self.ans

    def recursion(self, n, count: dict, parentheses: str):
        if count[")"] == n and count["("] == n:
            self.ans.append(parentheses)
            return

        if count["("] == n:
            parentheses = parentheses + ")"
            count[")"] += 1
            self.recursion(n, count, parentheses)

        if count["("] > count[")"]:
            count1 = copy.deepcopy(count)
            count1[")"] += 1
            parentheses1 = parentheses + ")"
            self.recursion(n, count1, parentheses1)
            count2 = copy.deepcopy(count)
            count2["("] += 1
            parentheses2 = parentheses + "("
            self.recursion(n, count2, parentheses2)

        if count["("] == count[")"]:
            parentheses = parentheses + "("
            count["("] += 1
            self.recursion(n, count, parentheses)
# Status: Memory Limit Exceeded
# Intuition: Recursion
# Note: deep copy 때문에 메모리 초과. recursion으로 간단히 되겠다고 생각했는데 생각보다 손이 많이 가서 별로인 것 같다.
#       다시 도전


# my solution
class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.recursion(0, 0, "")
        return self.ans

    def recursion(self, o, c, s):
        if o == self.n and c == self.n:
            self.ans.append(s)
            return

        if o == self.n:
            self.recursion(o, c + 1, s + ")")
        else:
            if o > c:
                self.recursion(o, c + 1, s + ")")
                self.recursion(o + 1, c, s + "(")
            else:
                self.recursion(o + 1, c, s + "(")
# Status: Accepted
# Algorithm: Recursion
# Note: 사실 위랑 같은 원리. 처리가 귀찮은 부분들을 바꿔줬다.
# Runtime: 36ms(top 46.3 %)
