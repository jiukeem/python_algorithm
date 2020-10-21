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
