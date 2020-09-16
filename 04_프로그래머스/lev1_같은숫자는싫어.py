# 너무 힘들어서 자신감 회복하려고 lev1만 골라푸는 중
def solution(arr):
    ans = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            ans.append(arr[i])

    return ans