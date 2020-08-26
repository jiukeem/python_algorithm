def swap(complete_binary_tree, index1, index2):
    complete_binary_tree[index1], complete_binary_tree[index2] = \
    complete_binary_tree[index2], complete_binary_tree[index1]

def heapify(tree, index, tree_size):
    left_child_index = index * 2
    right_child_index = index * 2 + 1

    max_index = index
    if left_child_index <= tree_size:
        if tree[max_index] < tree[left_child_index]:
            max_index = left_child_index

    if right_child_index <= tree_size:
        if tree[max_index] < tree[right_child_index]:
            max_index = right_child_index

    if max_index != index:
        swap(tree, index, max_index)
        heapify(tree, max_index, tree_size)

def reverse_heapify(tree, index):
    # 삽입하는 노드를 힙 속성을 지키는 위치로 이동
    parent_index = index // 2
    if parent_index < 1:
        return
    if tree[parent_index] < tree[index]:
        swap(tree, parent_index, index)
        reverse_heapify(tree, parent_index)


class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        # 데이터를 추가하면 힙속성에 맞는 위치로 옮겨주는 함수
        self.heap.append(data)
        index = len(self.heap) - 1
        reverse_heapify(self.heap, index)

    def extract_max(self):
        # 최우선 순위 데이터를 추출
        # 크기가 곧 우선순위인 경우(클수록 우선순위가 높음)
        swap(self.heap, 1, len(self.heap)-1)
        max_value = self.heap.pop()
        heapify(self.heap, 1, len(self.heap))

        return max_value

    def __str__(self):
        return str(self.heap)


# 실행 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)