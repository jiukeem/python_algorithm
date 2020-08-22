# 리스트를 파라미터로 받으며 리스트는 매일의 이익으로 구성되어 있다.
# 수익 합이 가장 큰 구간을 찾아서 수익값을 리턴

# 브루트포스 O(n^2)
def sublist_max(profits):
    max_profit = profits[0]
    for i in range(len(profits)):
        for j in range(i, len(profits) + 1):
            max_profit = max(max_profit, sum(profits[i:j]))

    return max_profit

# divide and conquer를 이용해서 시간복잡도를 O(nlgn)으로 줄여보자
def combine(profits, start, end):
    point = (start + end) // 2 + 1
    max_profit = 0

    for i in range(start, point):
        for j in range(point, end):
            max_profit = max(max_profit, sum(profits[i:j+1]))

    return max_profit

def sublist_max(profits, start, end):
    if end - start <= 0:
        return profits[start]

    mid = (start + end) // 2
    return max(combine(profits, start, end),
    sublist_max(profits, start, mid),
    sublist_max(profits, mid+1, end))
# i랑 j 범위를 반으로 줄였지만 그래봤자 n/2 * n/2 이니 시간복잡도는 O(n^2)다...
# 심지어 재귀를 lg(n)만큼 호출하니 n^2 * lg(n) 됨... 똥망
# sublist_max는 제대로 구현했고 combine이 잘못됨


# 제대로된 divide and conquer 구현
def max_crossing_sum(profits, start, end):
    mid = (start + end) // 2

    left_max = profits[mid]
    for i in range(mid, start - 1, -1):
        left_max = max(left_max, sum(profits[i: mid + 1]))

    right_max = profits[mid + 1]
    for j in range(mid + 1, end + 1):
        right_max = max(right_max, sum(profits[mid + 1: j + 1]))

    return left_max + right_max


def sublist_max(profits, start, end):
    if end - start <= 0:
        return profits[end]

    mid = (start + end) // 2
    return max(
        max_crossing_sum(profits, start, end),
        sublist_max(profits, start, mid),
        sublist_max(profits, mid + 1, end))
# 시간복잡도 O(nlgn)


# 세상에 O(n)으로도 줄일 수 있다 이게 어떻게 가능하지?
def sublist_max(profits):
    prev = profits[0]
    output = profits[0]
    for i in range(1, len(profits)):
        output = max(output, prev)
        prev = max(prev + profits[i], profits[i])

    return output
# 진짜.. 말도 안돼ㅜㅜ

print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))