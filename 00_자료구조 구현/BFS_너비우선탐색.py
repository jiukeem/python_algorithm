from collections import deque
from graph_그래프 import create_station_graph
# graph 파일에서 만든 지하철 스테이션 그래프를 가져옴

def bfs(graph, start_node):
    queue = deque()

    for station_node in graph.values():
        station_node.visited = False
        # 일단 모든 노드에 대해 방문하지 않음으로 표시

    queue.append(start_node)
    start_node.visited = True
    # 큐에 시작노드를 추가해주고 방문여부를 바꿔줌

    while queue:
        node_to_search = queue.popleft()
        for connected_node in node_to_search.adjacent_stations:
            if connected_node.visited == False:
                connected_node.visited = True
                queue.append(connected_node)


stations = create_station_graph("./stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)