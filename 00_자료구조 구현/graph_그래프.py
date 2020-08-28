# 지하철역을 이용해서 그래프를 만들어보자.
# 무방향그래프이고, 인접리스트를 사용함

class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = False
        # 탐색할 때 방문여부 저장
        self.predecessor = None
        # bfs를 통한 최단경로탐색시 사용

    def add_connection(self, station_to_connect):
        # 무방향그래프이므로 양쪽 노드에 서로를 추가
        self.adjacent_stations.append(station_to_connect)
        station_to_connect.adjacent_stations.append(self)

    def __str__(self):
        # 노드의 역 이름 : 인접한 역들 식으로 출력됨
        str = f'{self.station_name}: '

        for station in self.adjacent_stations:
            str += f'{station.station_name} '

        return str


def create_station_graph(input_file):
    # 같은 폴더내에 위치한 stations 텍스트파일을 읽어와서 노드로 생성후, 노드들을 저장한 딕셔러리를 return
    stations = {}

    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:
            previous_station = None
            subway_line = line.strip().split('-')
            # 앞뒤 띄어쓰기 벗기고 -기준으로 쪼갬

            for name in subway_line:
                station_name = name.strip()
                # 역이름 앞뒤에 스페이스가 있을지 모르니 한번 더 처리
                if station_name not in stations:
                    current_station_node = StationNode(station_name)
                    stations[station_name] = current_station_node
                else:
                    current_station_node = stations[station_name]

                if previous_station is not None:
                    stations[station_name].add_connection(previous_station)

                previous_station = current_station_node

    return stations

stations = create_station_graph("./stations.txt")

# stations에 저장한 역과 인접역(인접리스트)들 이름 출력
for station in stations.keys():
    print(stations[station])