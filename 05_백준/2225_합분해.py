# coding=utf-8

# my solution
N, K = map(int, input().split())

def solution(N, K):
    if K == 0:
        return 0
    if K == 1:
        return 1
    if K == 2:
        return N + 1
    else:
        answer = 0
        for n in range(N + 1):
            answer += solution(N - n, max(K - 1, 0))

        return answer % 1000000000

print(solution(20, 2))
print(solution(1, 2))
print(solution(1, 3))
print(solution(0, 3))
print(solution(0, 4))
print(solution(2, 1))
print(solution(2, 2))
print(solution(2, 3))
print(solution(2, 4))
print(solution(2, 5))
print(solution(5, 2))
print(solution(5, 3))
#print(solution(87, 65))
# Status: Timeout
# Algorithm: Recursion
# Note: 백준은 타임아읏을 따로 알려주는지 '틀렸습니다'로 퉁치는지 잘 모르겠넴.
#       위의 tc를 전부 통과하는 걸 보면 코드가 틀린건 아닌거 같은데 87 65 에서 시간이 너무 오래걸린다. 아마 타임아웃인 것 같다.
#       아 백준도 타임아웃이면 타임아웃이라고 뜬다고 한다. 웬만한 반례는 체크했다고 생각했는데 어디서 틀린걸까
#       def solution만 하고 펑션콜을 하지않아서 틀린거였다=.= 아예 아무것도 return 하지 않는 코드를 몇 번이나 제출한 것.
#       프로그래머스는 제출을 하면 자체적으로 펑션 콜을 진행해서 평가하기 때문에 습관적으로 이렇게 제출했다.
#       한 플랫폼만 쓰다보니 생긴 문제.... 이 코드는 틀리지는 않았고 시간초과가 뜬다.
#       이제 시간제한을 만족해야 하니 dp로 다시 풀어보자. overlapping subproblem 들을 합쳐합쳐

# my solution 2
def solution_2(N, K):
    if N == 0:
        return 1
    if K == 0:
        return 0

    table = [[None] * (K + 1) for _ in range(N + 1)]
    for k in range(K + 1):
        table[0][k] = 1
        table[1][k] = k
    for n in range(N + 1):
        table[n][0] = 0
        table[n][1] = 1

    for n in range(2, N + 1):
        for k in range(2, K + 1):
            table[n][k] = table[n - 1][k] + table[n][k - 1]

    return table[N][K] % 1000000000
# Status: Accepted
# Algorithm: Dynamic Programming (tabulation)
# Note: table 크기를 200으로 하면 위의 예외처리 N == 0, K == 0 을 안해줘도 되지만 공간낭비가 심할 것 같아 이렇게 했다.
#       이건 딴 얘긴데 백준은 return이 아니라 출력(print)이네...ㅎㅎㅎ 아까운 내 시간...ㅠㅠ














