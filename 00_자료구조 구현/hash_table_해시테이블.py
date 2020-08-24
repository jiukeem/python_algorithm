# 파이썬 리스트 자료형을 이용해서 구현

from chaining용 연결리스트 import LinkedList
# 이거 왜 안불러와지지ㅜㅜ


class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity
        self._table = [LinkedList() for _ in range(self._capacity)]
        # 해시테이블이 사용할 파이썬 리스트이며, 각 인덱스에 비어있는 연결리스트를 생성
        # 외부에서 접근하면 안된다는 걸 알릴 때는 앞에 _를 붙여줌

    def _hash_function(self, key):
        return hash(key) % self._capacity
        # hash는 파이썬 내장함수로, 불변타입형 값에 고유 정수값을 부여함

    def get_linked_list_for_key(self, key):
        # 탐색, 삽입 연산에서 쓰이는 헬퍼메소드
        # key에 해당하는 인덱스의 연결리스트를 return
        index = self._hash_function(key)
        return self._table[index]

    def _look_up_node(self, key):
        # 헬퍼 메소드2
        # 연결리스트에서 해당 키를 가진 노드가 있는지 확인
        # 없으면 None 을 return
        linked_list = self.get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def look_up_value(self, key):
        # 탐색 연산
        node_with_the_key = self._look_up_node(key)
        if node_with_the_key is None:
        # 키에 해당하는 노드가 없는 경우
            return None
        else:
            return node_with_the_key.value

    def insert(self, key, value):
        # 삽입 연산
        node_with_the_key = self._look_up_node(key)
        if node_with_the_key is None:
            linked_list = self.get_linked_list_for_key(key)
            linked_list.append(key, value)
        else:
            node_with_the_key.value = value

    def delete_by_key(self, key):
        # 삭제 연산
        node_with_the_key = self._look_up_node(key)
        linked_list = self._get_linked_list_for_key(key)
        if node_with_the_key is not None:
            linked_list.delete(node_with_the_key)

    def __str__(self):
        str = ''
        for linked_list in self._table:
            str += str(linked_list)
            # linked_list는 LinkedList 클래스이므로
            # 해당 클래스 내에서 설정한 __str__ 이 바로 적용된다.

        return str
