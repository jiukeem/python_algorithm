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
                connected_node.predecessor = node_to_search
                queue.append(connected_node)

def back_track(destination_node):
    # 최단 경로를 찾는 백트래킹 함수
    str = ''
    iterator = destination_node

    while iterator is not None:
        str = f'{iterator.station_name} {str}'
        iterator = iterator.predecessor

    return str


stations = create_station_graph("./stations.txt")

bfs(stations, stations["을지로3가"])
# 지하철 그래프에서 을지로3가역을 시작노드로 bfs 실행

print(back_track(stations["강동구청"]))
# 을지로3가에서 강동구청역까지 최단 경로 출력