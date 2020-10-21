# 선형 탐색
def linear_search(list, value):
    for element in list:
        if element == value:
            return value
    return None
# Time Complexity: O(n)


# 이진 탐색
def binary_serach(sorted_list, value):
    n = len(sorted_list)
    if n == 0:
        return None

    mid = sorted_list[n // 2]
    if mid == value:
        return mid
    elif mid < value:
        return binary_serach(sorted_list[n//2 + 1:], value)
    else:
        return binary_serach(sorted_list[:n//2], value)

array = [1, 3, 4, 7, 10, 17, 24, 75, 87, 92, 98, 106, 109, 201, 492, 589]
print(binary_serach(array, 12))
# Time Complexity: O(lg(n))

#
