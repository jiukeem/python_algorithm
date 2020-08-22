# 브루트포스 O(n^2)
def max_profit(stock_list):
    max_profit = stock_list[1] - stock_list[0]
    for i in range(len(stock_list)):
        for j in range(i+1, len(stock_list)):
            max_profit = max(max_profit, stock_list[j] - stock_list[i])

    return max_profit


# divide and conquer로 가능할까?
def cross_max_profit(stock_list):
    mid = len(stock_list) // 2
    left_value = min(stock_list[:mid])
    right_value = max(stock_list[mid:])

    return right_value - left_value

def max_profit(stock_list):
    if len(stock_list) == 2:
        return stock_list[-1] - stock_list[0]

    mid = len(stock_list) // 2
    return max(
        cross_max_profit(stock_list),
        max_profit(stock_list[:mid]),
        max_profit(stock_list[mid:]))
# 앞에서 한 방식으로 O(nlgn)을 만들어보려고 했는데 얘는 len =1 인 경우 제대로 작동하지 않는 문제라서 실패


# 코드잇 해답
def max_profit(stock_list):
    min_num_so_far = min(stock_list[0], stock_list[1])
    max_profit_so_far = stock_list[1] - stock_list[0]

    for i in range(2, len(stock_list)):
        max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_num_so_far)
        min_num_so_far = min(min_num_so_far, stock_list[i])

    return max_profit_so_far
# 와... 이게 이렇게 간단히 된다고? 진짜 대단하다 O(n)


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))