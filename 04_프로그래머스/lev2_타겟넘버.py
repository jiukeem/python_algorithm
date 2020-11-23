# my solution
class Search:
    def __init__(self):
        self.ans = 0

    def dfs(self, numbers, target):
        if sum(numbers) < abs(target):
            # 불가능한 경우의 수일 경우 굳이 끝까지 dfs를 돌지 않게 하기 위함
            # 이 부분이 없어도 코드는 돌아지만 인풋 양이 많아질수록 시간 절약의 효과가 있을 것 같다.
            return
        if len(numbers) == 1:
            if numbers[0] == abs(target):
                self.ans += 1
            return
        else:
            self.dfs(numbers[1:], target - numbers[0])
            self.dfs(numbers[1:], target + numbers[0])

def solution(numbers, target):
    sol = Search()
    sol.dfs(numbers, target)
    return sol.ans
# Status: Accpeted
# Algorithm: DFS
# Note: 흠 class말고 함수 두개로도 짤 수 있으면 좋을텐데
#       코드 자체는 깔끔하게 잘 짠 것 같다.
#       클래스를 쓴 이유는 ans 때문이었는데 global을 쓰면 클래스 없이도 짤 수 있다.
#       그냥 바깥에 ans = 0 해두고 함수 내부에서 global ans 이렇게 선언해주면 된다.


# 다른 사람의 풀이
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])
# 원리는 내 풀이와 같다. 나는 ans 관리 때문에 클래스까지 쓰게 됐는 그냥 +로 구현해도 가능하다.
# + 등의 사칙연산을 쓰면 대신 내 머리가 좀 더 복잡해진다.


# 1123 한번 더
def solution(numbers, target):
    if sum(numbers) < target:
        return 0
    if len(numbers) == 1:
        return 1 if numbers[0] == abs(target) else 0
    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])
# Status: Accepted
