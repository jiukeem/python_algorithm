# heapify 구현 (오름차순 정렬용)
def swap(complete_binary_tree, index1, index2):
    complete_binary_tree[index1], complete_binary_tree[index2] = \
    complete_binary_tree[index2], complete_binary_tree[index1]

def heapify(tree, index, tree_size):
    left_child_index = index * 2
    right_child_index = index * 2 + 1

    max_index = index
    if left_child_index < tree_size:
        if tree[max_index] < tree[left_child_index]:
            max_index = left_child_index

    if right_child_index < tree_size:
        if tree[max_index] < tree[right_child_index]:
            max_index = right_child_index

    if max_index != index:
        swap(tree, index, max_index)
        heapify(tree, max_index, tree_size)

def heapsort(tree):
    tree_size = len(tree)

    # 리스트를 힙으로 만든다
    for i in range(tree_size-1, 0, -1):
        heapify(tree, i, tree_size)

    for i in range(tree_size-1, 1, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i)


data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)