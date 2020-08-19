# tabulation 방식으로 피보나치 수열 값 구하는 함수 구현

def fib_tab(n):
    table = {}
    for i in range(1, n + 1):
        if i < 3:
            table[i] = 1
        else:
            table[i] = table[i - 1] + table[i - 2]

    return table[n]


# 공간최적화 O(1)도 가능하다
def fib_optimized(n):
    current = 1
    prev = 0
    for _ in range(n - 1):
        current, prev = current + prev, current

    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
