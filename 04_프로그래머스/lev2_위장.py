# my solution
from collections import defaultdict

def solution(clothes):
    table = defaultdict(list)
    for cloth, name in clothes:
        table[name].append(cloth)

    n = len(table)
    # 옷 종류의 개수. 최소1개부터 최대n개까지 착용가능

    from itertools import combinations
    res = 0
    for i in range(1, n + 1):
        comb = combinations(table.keys(), i)
        for set in comb:
            temp = 1
            for j in range(i):
                temp *= len(table[set[j]])
            res += temp

    return res
# 30개의 tc 중 1개가 타임아웃이 난다.

def solution(clothes):
    table = defaultdict(list)
    for cloth, name in clothes:
        table[name].append(cloth)

    ans = 1
    for cloth in table.values():
        ans *= (len(cloth) + 1)

    return ans - 1
# Intuition: 안입는 경우도 한가지 경우로 생각해서 value 개수 + 1 을 다 곱해준다.
#            그리고 전부 다 안입은 경우을 제외하기 위해 1을 빼주면 완성


# 다른 사람의 코드
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
# 우와우 사실상 원리는 내것과 똑같음. 람다와 reduce를 좀 더 연습해야겠다.