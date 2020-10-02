# my solution
def solution(N, stages):
    stages = sorted(stages, reverse=True)
    failure_rate = {}

    for i in range(1, N + 1):
        numerator, denominator = 0, len(stages)
        while stages and stages[-1] == i:
            stages.pop()
            numerator += 1
        failure_rate[i] = numerator / denominator if denominator != 0 else 0

    return sorted(failure_rate.keys(), key=lambda x: failure_rate[x], reverse=True)
# Status: Accepted
# Note: time complexity는 O(n)이고 pop을 이용해서 깔끔하게 잘 짠 것 같다. 뿌듯해
#       다른 사람 풀이를 보니 while이 돌 때마다 numerator += 1 을 하는대신 numerator = stages.count(i) 로 할 수 있다.
#       내가 잘쓰지 않는 메소드라 쓸 생각을 못했는데 이것도 괜찮겠다. 다만 그 경우에는 pop을 안쓰니 연산시간이 증가할 듯? -> 오! 해보니 내 방식이 압도적으로 빠르다. 45ms vs 1385ms 다ㅎㅎ

