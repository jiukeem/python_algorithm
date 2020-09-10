# my solution
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [0]

    for i in range(1, n - 1):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    for idx in stack:
        answer[idx] = n - 1 - idx

    return answer
# Status: Accepted
# Algorithm: Stack
# Time Complexity: O(n)

