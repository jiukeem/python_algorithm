def find_left_child(complete_binary_tree, index):
    left_child = index * 2
    if left_child < len(complete_binary_tree):
        return complete_binary_tree[left_child]
    return None
    # 없을 경우 None 을 반환

def find_right_child(complete_binary_tree, index):
    right_child = index * 2 + 1
    if right_child < len(complete_binary_tree):
        return complete_binary_tree[right_child]
    return None

def find_parent(complete_binary_tree, index):
    parent = index // 2
    return complete_binary_tree[parent]


# heapify 구현
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
