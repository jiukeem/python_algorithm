# my solution
def solution(arr, divisor):
    ans = [i for i in arr if i % divisor == 0]
    if len(ans) == 0:
        return [-1]
    return sorted(ans)


# or을 사용하면 한줄에 가능
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]
