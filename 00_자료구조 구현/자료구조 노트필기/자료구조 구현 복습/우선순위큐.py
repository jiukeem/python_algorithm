# 힙으로 구현
# 리스트로 구현된 완전이진트리를 받는다.

# 리스트에 힙속성 부여(무작위 리스트에 이걸 맨 끝 인덱스부터 n번 돌려야 힙 완성)
def heapify(tree, idx, end_idx):
    left_child_idx = idx * 2
    right_child_idx = idx * 2 + 1

    max_idx = idx
    if left_child_idx < end_idx and tree[left_child_idx] > tree[max_idx]:
        max_idx = left_child_idx

    if right_child_idx < end_idx and tree[right_child_idx] > tree[max_idx]:
        max_idx = right_child_idx

    if max_idx != idx:
        tree[max_idx], tree[idx] = tree[idx], tree[max_idx]
        heapify(tree, max_idx, end_idx)

def heapify_upward(heap, idx):
    parent_idx = idx // 2
    if parent_idx < 1:
        return
    if heap[parent_idx] < heap[idx]:
        heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        heapify_upward(heap, parent_idx)


class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        heapify_upward(self.heap, len(self.heap) - 1)

    def extract_max(self):
        idx = len(self.heap) - 1
        self.heap[1], self.heap[idx] = self.heap[idx], self.heap[1]
        max_value = self.heap.pop()
        heapify(self.heap, 1, len(self.heap) - 1)
        return max_value

    def __str__(self):
        return str(self.heap)

pq = PriorityQueue()
pq.insert(3)
pq.insert(2)
pq.insert(45)
pq.insert(17)
pq.insert(31)
pq.insert(106)
pq.insert(63)
pq.insert(5)
print(pq.extract_max())
print(pq.extract_max())
print(pq.extract_max())
