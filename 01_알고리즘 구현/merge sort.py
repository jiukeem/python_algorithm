def merge(list1, list2):
    output = []
    while list1 and list2:
        if list1[0] <= list2[0]:
            output.append(list1[0])
            del list1[0]
        else:
            output.append(list2[0])
            del list2[0]

    rest = list1 or list2
    output += rest
    return output


# 합병 정렬
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = len(my_list) // 2
    return merge(merge_sort(my_list[:mid]), merge_sort(my_list[mid:]))


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
