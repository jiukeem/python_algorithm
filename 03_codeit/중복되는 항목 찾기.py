# n+1 길이의 리스트에 1부터 n까지 임의의 자연수가 들어있다. 즉 최소 한 개의 수는 두번이상 들어있다.
# 이 때 그 값을 구하는데 만약 조건을 만족하는 수가 여러개라면 그 중에 한개만 return해도 오케이
# ex [1, 4, 1, 2, 2]에서 1 혹은 2를 return


# 브루트 포스 O(n^2_
def find_same_number(some_list):
    for i in range(len(some_list)):
        for j in range(i+1, len(some_list)):
            if some_list[i] == some_list[j]:
                return some_list[i]


# O(n)의 공간을 할당하면서 대신 시간복잡도를 O(n)으로 줄임
def find_same_number(some_list):
    nums = []
    for num in some_list:
        if num in nums:
            return num
        nums.append(num)


