def solution(n):
    length = len(str(n))
    ans = [n % pow(10, i) // pow(10, i-1) for i in range(1, length+1)]
    return ans


def solution(n):
    ans = [int(i) for i in reversed(str(n))]
    return ans