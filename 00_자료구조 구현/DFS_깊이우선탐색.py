from collections import deque
from graph_그래프 import *
# graph 파일에서 만든 지하철 스테이션 그래프를 가져옴

def dfs(graph, start_node):
    stack = deque()
    # 리스트 사용해도 되긴함

    for station_node in graph.values():
        station_node.visited = 0

    stack.append(start_node)
    start_node.visited = 1
    # 큐에 시작노드를 추가해주고 방문여부를 바꿔줌

    while stack:
        node_to_search = stack.pop()
        node_to_search.visited = 2
        # 스택에서 뺄 때 방문여부를 2로 수정
        for connected_node in node_to_search.adjacent_stations:
            if connected_node.visited == 0:
                stack.append(connected_node)
                connected_node.visited = 1
                # 방문한 적 없으면 stack에 추가하고 방문여부를 1로 바꿔줌


stations = create_station_graph("./stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
dfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)