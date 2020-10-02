# my solution
import re

def solution(dartResult):
    p = re.compile('(\d+)([SDT])([*#]*)')
    darts = p.findall(dartResult)

    ans = []
    for d in darts:
        (n, bonus, option) = d
        n = int(n)

        # bonus check
        if bonus == 'D':
            n = n ** 2
        elif bonus == 'T':
            n = n ** 3

        # option check
        if option == '*':
            n *= 2
            if ans:
                ans[-1] *= 2
        elif option == '#':
            n *= -1

        ans.append(n)

    return sum(ans)
# Status: Accepted
# Note: 카카오는 언제나 정규표현식을 요하는 문제를 한개씩 내는 듯 하다.
#       정규표현식이 생소한건 아니지만 사용할 일이 별로 없어서 언제나 한번씩 구글링하면서 정독하게 된당
#       내가 쓴건 grouping 과 findall method
#       깔끔하게 잘 짠 것 같다.


# 다른사람의 solution
import re

def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    darts = p.findall(dartResult)
    ans = [None] * len(darts)

    for i in range(len(darts)):
        if darts[i][2] == '*' and i > 0:
            ans[i-1] *= 2
        ans[i] = int(darts[i][0]) ** bonus[darts[i][1]] * option[darts[i][2]]

    return sum(ans)
# 같은 정규표현식인데 일단 [*#]* 보다 [*#]? 이 더 맞는 것 같다. (같은 답을 내놓긴하지만)
# 그리고 bonus와 option을 dict로 만들어서 쓰니 더 간결하다
# 더 줄이려고 하면 ans를 만들지 않고 dart에 업데이트를 할 수도 있는데 난 그것까진 오류날까 살떨려서 못하겠다이



