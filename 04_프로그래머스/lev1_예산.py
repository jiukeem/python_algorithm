# my solution
def solution(d, budget):
    ans = 0
    for i in sorted(d):
        if i <= budget:
            ans += 1
            budget -= i
        if budget < i or budget < 0:
            break
    return ans
# Status: Accepted
# Note: while 문으로 하는게 더 깔끔할까? 한번 더 짜보자


def solution(d, budget):
    tot = 0
    for i, n in enumerate(sorted(d)):
        tot += n
        if tot > budget:
            return i

    return len(d)
# Status: Accepted
# Note: 더 깔끔하긴한데 위의 코드보다 오래 걸리네. 흠 둘다 O(n)이라서 큰 차이는 없을 듯 하다.
#       d와 budget의 범위가 크지않아서 정확한 비교는 어렵다.


# 다른 사람의 solution
def solution(d, budget):
    d, s = sorted(d), sum(d)
    while budget < s:
        s -= d.pop()

    return len(d)
# 내 두번째 코드와 비슷하지만 더 나은 것 같다. (내꺼는 더해나가는 방식, 이건 총합에서 빼나가는 방식)
# return이 한개로 통일되는게 깔끔하다.