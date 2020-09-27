def solution(x):
    n = sum([int(i) for i in str(x)])
    return x % n == 0
