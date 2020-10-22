# 선택정렬
def selection_sort(list):
    ans = []
    while list:
        min_value = list[0]
        for num in list:
            min_value = min(min_value, num)
        ans.append(min_value)
        list.remove(min_value)

    return ans

array = [3, 6, 2123, 4, 76, 47, 2, 94, 143, 2, 5]
print(selection_sort(array))
# Time Complexity: O(n^2)
# enumerate로 idx를 가져가면 remove 대신 del을 사용할 수 있긴하지만 둘 다 시간복잡도는 O(n^2)이므로 그냥 remove를 사용함


# 삽입정렬
def insertion_sort(list):
    for i in range(0, len(list)):
        while list[i - 1] > list[i] and i > 0:
            list[i - 1], list[i] = list[i], list[i - 1]
            i -= 1

    return list
array = [3, 6, 2123, 4, 76, 47, 2, 94, 143, 2, 5]
print(insertion_sort(array))
# Time Complexity: O(n^2)

# 합병정렬
def merge(list_1, list_2):
    ans = []
    while list_1 and list_2:
        if list_1[0] < list_2[0]:
            ans.append(list_1[0])
            del list_1[0]
        else:
            ans.append(list_2[0])
            del list_2[0]

    ans += list_1 or list_2
    return ans

def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        mid = len(list) // 2
        return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))

array = [3, 6, 2123, 4, 76, 47, 2, 94, 143, 2, 5]
print(merge_sort(array))
# Time Complexity: O(n(lg(n)) 깊이(divide)가 lg(n)에 비례하고 각 깊이에서 합병은 n 이므로 nlg(n)


# 퀵 정렬
def partition(list):
    pivot = list[-1]
    small, big = [], []
    for num in list[:-1]:
        if num < pivot:
            small.append(num)
        else:
            big.append(num)

    return small + [pivot] + big, len(small)

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        list, pivot_idx = partition(list)
        return quick_sort(list[:pivot_idx]) + [list[pivot_idx]] + quick_sort(list[pivot_idx+1:])

array = [3, 6, 2123, 4, 76, 47, 2, 94, 143, 2, 5]
print(quick_sort(array))
# Time Complexity: O(n(lg(n))


# 퀵 정렬 in-place 로
def partition_2(list, start, end):
    i = start
    b = start
    pivot = list[end]

    while i < end:
        if list[i] < pivot:
            list[i], list[b] = list[b], list[i]
            b += 1
        i += 1

    list[b], list[end] = list[end], list[b]
    return b

def quick_sort_2(list, start, end):
    if end - start < 1:
        return
    else:
        b = partition_2(list, start, end)
        quick_sort_2(list, start, b - 1)
        quick_sort_2(list, b + 1, end)
        return list

array = [3, 6, 2123, 4, 76, 47, 2, 94, 143, 2, 5]
print(quick_sort_2(array, 0, len(array) - 1))
# 역시 in-place는 어려워


# 힙 정렬
def heapify(tree, idx, tree_size):
    left_child_idx = idx * 2
    right_child_idx = idx * 2 + 1

    max_idx = idx
    if left_child_idx < tree_size:
        if tree[max_idx] < tree[left_child_idx]:
            max_idx = left_child_idx

    if right_child_idx < tree_size:
        if tree[max_idx] < tree[right_child_idx]:
            max_idx = right_child_idx

    if max_idx != idx:
        tree[max_idx], tree[idx] = tree[idx], tree[max_idx]
        heapify(tree, max_idx, tree_size)

def heapify_upward(tree, idx, tree_size):
    parent_idx = idx // 2
    if parent_idx > 0 and tree[parent_idx] > tree[idx]:
        tree[parent_idx], tree[idx] = tree[idx], tree[parent_idx]
        print(tree)
        heapify_upward(tree, parent_idx, tree_size)

def insert(heap, num):
    heap.append(num)
    heap = [None] + heap
    print(heap)
    heap_size = len(heap)
    heapify_upward(heap, heap_size-1, heap_size)
    return heap[1:]

def heap_sort(tree):
    tree_size = len(tree)

    for i in range(tree_size-1, 0, -1):
        heapify(tree, i, tree_size)

    for i in range(tree_size-1, 1, -1):
        tree[i], tree[1] = tree[1], tree[i]
        heapify(tree, 1 ,i)

    return tree[1:]

array = [None, 3, 6, 2123, 4, 76, 47, 2, 94, 143, 2, 5]
sorted_arr = heap_sort(array)
print(sorted_arr)
# Time Complexity: 맨 아래 포문을 보면 heapify 의 시간복잡도 O(lg(n)) * 포문 O(n) = O(n * lg(n))


# 힙 정렬 헷갈려서 한번 더
def heapify_2(tree, idx, end):
    left_child_idx = idx * 2
    right_child_idx = idx * 2 + 1

    max_idx = idx
    if left_child_idx < end and tree[left_child_idx] > tree[max_idx]:
        max_idx = left_child_idx

    if right_child_idx < end and tree[right_child_idx] > tree[max_idx]:
        max_idx = right_child_idx

    if max_idx != idx:
        tree[max_idx], tree[idx] = tree[idx], tree[max_idx]
        heapify_2(tree, max_idx, end)

def heap_sort_2(tree):
    tree = [None] + tree
    tree_size = len(tree)

    # 힙속성을 부여하는 작업
    for i in range(tree_size - 1, 0, -1):
        heapify_2(tree, i, tree_size)

    for i in range(tree_size - 1, 1, -1):
        tree[1], tree[i] = tree[i], tree[1]
        heapify_2(tree, 1, i)

    return tree[1:]
array = [3, 6, 2123, 4, 76, 47, 2, 94, 143, 2, 5]
print(heap_sort_2(array))