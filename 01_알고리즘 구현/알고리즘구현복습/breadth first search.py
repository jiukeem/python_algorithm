# 그래프 구현에서 만든 stations 를 그대로 사용
# stations는 dict이며,stations[name] = node 로 저장되어 있음

# bfs는 큐를 사용하므로 데크 사용
from collections import deque

def bfs(graph, start_node):
    queue = deque()

    for station_node in graph.values():
        station_node.visited = False

    queue.append(start_node)
    start_node.visited = True

    while queue:
        node_to_search = queue.popleft()
        for connected_node in node_to_search.adjacent_stations:
            if connected_node.visited == False:
                connected_node.visited = True
                queue.append(connected_node)

# predecessor 프로퍼티를 사용하는 최단경로용 bfs 한번더
def bfs(graph, start_node):
    queue = deque()

    for station_node in graph.values():
        station_node.visited = False

    queue.append(start_node)
    start_node.visited = True

    while queue:
        node_to_search = queue.popleft()
        for connected_node in node_to_search.adjacent_stations:
            if connected_node.visited == False:
                connected_node.visited = True
                connected_node.predecessor = node_to_search
                queue.append(connected_node)

def back_track(destination_node):
    to_print = ""
    iter = destination_node

    while iter:
        to_print += destination_node.station_name
        iter = iter.predecessor

    return to_print