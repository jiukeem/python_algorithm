# memoization 방식으로 피보나치 수열 값 구하는 함수 구현

# 내 풀이
def fib_memo(n, cache):
    if n < 3:
        return 1

    if n in cache:
        return cache[n]

    return fib_memo(n - 2, cache) + fib_memo(n - 1, cache)


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    for i in range(n):
        if i < 3:
            fib_cache[i] = 1
        else:
            fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2]

    return fib_memo(n, fib_cache)
# 코드는 제대로 짰지만 왜 함수가 두개로 나뉘는지에 대한 파악을 제대로 못했다.


# 코드잇 풀이
def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1

    # 이미 n번째 피보나치를 계산했으면:
    # 저장된 값을 바로 리턴한다
    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않았으면:
    # 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    # 계산한 값을 리턴한다
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)
# fib에는 사전만 만들어주고 fib_memo에서 새로 연산되는 값들을 return 함과 동시에 cache에 저장해준다.
# 근데 함수 하나만 있으면 되는거 아냐..? 왜 이렇게 하시는거에요
# 아! 한개로 합쳐서 작성하면 재귀를 들어갈 때마다 cache가 빈 딕트로 정의되어버린다.
# dict는 재귀 바깥에서 계속 몸집을 불려나가야 하므로 이런 구조를 취하는 것