# 피보나치 수열 구현

# tabulation 방식
def tabulation(n):
    table = {
        1: 1,
        2: 1
    }
    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]

print(tabulation(3))
print(tabulation(4))
print(tabulation(5))
print(tabulation(6))
print(tabulation(7))

def tabulation_2(n):
    prev, current = 0, 1
    for _ in range(n - 1):
        prev, current = current, prev + current

    return current

print(tabulation_2(7))


# memoization 방식
class Memoization:
    def __init__(self):
        self.cache = {}
        for i in range(1,3):
            self.cache[i] = 1

    def fib(self, n):
        if n in self.cache.keys():
            return self.cache[n]
        else:
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]

memo = Memoization()
print(memo.fib(18))

# Time Complexity: O(n)
# 좀 헤맸는데 클래스로 구현하니 쉽다. self 프로퍼티가 있어서 간편하당


def fib(n, cache):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n-1, cache) + fib(n-2, cache)
        return cache[n]

cache = {1: 1, 2: 1}
print(fib(18, cache))
# 함수로도 성공했다. 나이스
