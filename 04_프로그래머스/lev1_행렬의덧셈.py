# my solution
import numpy as np

def solution(arr1, arr2):
    _arr1 = np.asarray(arr1)
    _arr2 = np.asarray(arr2)

    return np.array(_arr1 + _arr2).tolist()
# Status: Accepted
# Note: 넘파이 없이도 해보자


# my solution 2
def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])

    ans = []
    for _ in range(n):
        ans.append([0] * m)

    for i in range(n):
        for j in range(m):
            ans[i][j] = arr1[i][j] + arr2[i][j]

    return ans
# Status: Accepted
# 다른 사람의 풀이를 보니 ans를 만들지 않고 arr1에 더해주는게 더 낫겠다.

def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])

    for i in range(n):
        for j in range(m):
            arr1[i][j] += arr2[i][j]

    return arr1
# Status: Accepted


# 다른 사람의 solution
def solution(arr1, arr2):
    ans = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return ans
# 뜨아 이렇게 깔끔하게 되네.