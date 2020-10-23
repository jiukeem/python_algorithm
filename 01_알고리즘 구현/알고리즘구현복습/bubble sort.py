def swap(list, idx1, idx2):
    list[idx1], list[idx2] = list[idx2], list[idx1]

def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                swap(list, j, j + 1)

    return list

array = [4, 5, 1, 87, 23, 103, 143, 21, 9, 43, 5]
print(bubble_sort(array))
