from collections import deque

def solution(progresses, speeds):
    complete = deque()
    for prog, speed in zip(progresses, speeds):
        i = 0
        while prog < 100:
            prog += speed
            i += 1
        complete.append(i)

    answer = []
    count = 0
    while complete:
        prev = complete.popleft()
        count += 1
        while complete and prev >= complete[0]:
            complete.popleft()
            count += 1
        answer.append(count)
        count = 0

    return answer
# Status: Accepted
# Algorithm: Queue
# Time Complexity: O(n)
# Note: 일단 complete를 만들 때 while문을 돌릴 필요없다. (군더더기 1)
#       그리고 다 저장할 필요없이 위의 for문과 밑의 while문을 한번에 작업할 수 있다. (군더더기 2)


# 다른 좋은 코드
def solution(progresses, speeds):
    Q = []
    # list(list(int))의 형태. 안의 리스트는 [days_to_comp, count]
    for prog, speed in zip(progresses, speeds):
        days_to_left = -((prog - 100) // speed)
        # 나눗셈의 몫 + 1 을 하고 싶어서 p-100에 -를 취해줌
        if len(Q) == 0 or Q[-1][0] < days_to_left:
            # 아예 처음이거나, 가장 최근 것보다 더 오래걸리는 경우
            Q.append([days_to_left, 1])
        else:
            Q[-1][1] += 1

    return [q[1] for q in Q]