# 그래프 구현에서 만든 stations 를 그대로 사용
# stations는 dict이며,stations[name] = node 로 저장되어 있음

def dfs(graph, start_node):
    stack = []

    for station_node in graph.values():
        station_node.visited = 0

    stack.append(start_node)
    start_node.visited = 1

    while stack:
        node_to_search = stack.pop()
        node_to_search.visited = 2
        for connected_node in node_to_search.adjacent_stations:
            if connected_node.visited == 0:
                stack.append(connected_node)
                connected_node.visited = 1

# 재귀 사용한 dfs
def dfs_visit(adjacent_list, element, visited):
    visited.append(element)
    for next_ele in adjacent_list[element]
        if next_ele not in visited:
            dfs_visit(adjacent_list, next_ele, visited)

def dfs(adjacent_list, start):
    visited = []
    dfs_visit(adjacent_list, start, visited)
    return visited
