def solution(priorities, location):
    sorted_p = sorted(priorities, reverse=True)

    count = 0
    while priorities:
        first = priorities.pop(0)
        if first != sorted_p[0]:
            priorities.append(first)
            if location == 0:
                location = len(priorities)

        else:
            count += 1
            sorted_p.pop(0)
            if location == 0:
                return count
        location -= 1
# Status: Accepted
# Time Complexity: O(n)
# Note: 데크를 이용해서 popleft를 사용하면 더 빨라질거다. 근데 리스트로 주어진 priorities를 데크로 변환하는 데 더 오래 걸리려나?
#       if location == 0 문을 두 번 쓰는게 좀 못마땅한데 어떻게 한번으로 줄일 수 있을지 잘 모르겠다.
#       그 상위의 if에 따라 location이 0일 때 수행할 동작이 다른데 하나로 합칠 방법이 있을까?


# 다른 사람의 풀이
from collections import deque

def solution(priorities, location):
    Q = deque()
    for i, p in enumerate(priorities):
        Q.append((i, p))

    count = 0
    while Q:
        cur = Q.popleft()
        if any(cur[1] < q[1] for q in Q):
            Q.append(cur)
        else:
            count += 1
            if cur[0] == location:
                return count
# any를 이용한 깔끔한 방법 + 인덱스까지 같이 저장한 새로운 데크 생성
# 다만 any를 이용하면 요소를 꺼낼 때마다 포문을 돌리므로 나는 sorted 를 하나 두고 비교하는게 더 낫다고 생각함!