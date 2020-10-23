# 언제나 어려운 그래프를 한번 구현해볼까요 다 즐거우려고 하는건데 너무 힘들어하지 말자. 부족한 건 당연한 일이니까.
# 무방향 그래프 + 인접리스트를 사용하고 지하철 노선도 파일을 이용

class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = False
        self.predecessor = None
        # 최단경로탐색 시에 사용

    def add_connection(self, station_to_connect):
        # 무방향이므로 양쪽 노드에 서로를 추가
        self.adjacent_stations.append(station_to_connect)
        # 노드 이름이 아니라 노드 자체를 저장했다.
        station_to_connect.adjacent_stations.append(self)

    def __str__(self):
        to_print = self.station_name + ": "
        for station in self.adjacent_stations:
            to_print += station.station_name

        return to_print

def creat_station_graph(input_file):
    # 지하철역 정보 텍스트파일을 읽어와서 노드로 생성 후, 노드들을 해시테이블로 저장 후 return
    stations = {}

    with open(input_file) as station_raw_file:
        for line in station_raw_file:
            previous_station = None
            subway_line = line.strip().split('-')

            for name in subway_line:
                station_name = name.strip()
                if station_name not in stations:
                    current_station_node = StationNode(station_name)
                    stations[station_name] = current_station_node
                else:
                    current_station_node = stations[station_name]

                if previous_station is not None:
                    stations[station_name].add_connection(previous_station)

                previous_station = current_station_node

    return stations

stations = creat_station_graph("./stations.txt")
# 그래프 완성!

for station in stations.keys():
    print(stations[station])



# 혼자서 한번만 더 해보자
class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_list = []
        self.visited = False
        self.predecessor = None

    def add_connection(self, node_to_connect):
        self.adjacent_list.append(node_to_connect)
        node_to_connect.adjacent_list.append(self)

def gen_station_graph(input_file):
    stations = {}

    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:
            subway_line = line.strip().split('-')
            prev_station_node = None

            for name in subway_line:
                if name in stations:
                    current_node = stations[name]
                else:
                    current_node = StationNode(name)
                    stations[name] = current_node

                if prev_station_node:
                    stations[name].add_connection(prev_station_node)

                prev_station_node = current_node
    return stations


