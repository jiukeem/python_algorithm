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

