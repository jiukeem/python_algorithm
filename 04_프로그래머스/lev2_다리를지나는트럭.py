# my solution
from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    q, t = deque(), 1
    q.append((truck_weights.popleft(), t))

    while q:
        t += 1
        if t - q[0][1] == bridge_length:
            q.popleft()

        if truck_weights:
            if not q or sum([i[0] for i in q]) + truck_weights[0] <= weight:
                q.append((truck_weights.popleft(), t))
    return t
# Status: Accepted
# Note: 원리는 간단하다. 큐 안에 있는 트럭 무게의 총합과 새로들어올 트럭 무게의 합이 weight 보다 크지 않다면 큐에 추가
#       추가할 때는 (트럭무게, 들어온 시간) 튜플형태로 받아서 현재 경과시간 - 들어온 시각 이 다리 길이가 되면 popleft()
#       큐에 아무것도 안남으면 그 때의 경과시간 t를 return
#       다만 좀 못마땅한 부분은 큐에 원소하나를 넣어주고 시작해야 한다는 군더더기(세번째 줄 코드)
#       시간 효율성을 더 높이고 싶다면 sum을 한번만 계산하고 쁠마로 수정하면서 쓰면 된다. 지금은 시간초과가 안나서 그냥 sum()을 사용.
