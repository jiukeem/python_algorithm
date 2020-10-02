# my solution
def solution(n, arr1, arr2):
    _arr1 = [bin(i)[2:] for i in arr1]
    _arr2 = [bin(i)[2:] for i in arr2]
    for i in range(n):
        _arr1[i] = '0' * (n - len(_arr1[i])) + _arr1[i]
    for i in range(n):
        _arr2[i] = '0' * (n - len(_arr2[i])) + _arr2[i]

    ans = [''] * n
    for i in range(n):
        for j in range(n):
            ans[i] += ' ' if _arr1[i][j] == '0' and _arr2[i][j] == '0' else '#'

    return ans
# Status: Accepted
# Note: 음 밑에 포문돌리면서 ans 만드는 부분은 좋은데 위에 _arr 만드는 과정을 한 연산으로 해결할 수는 없을까?
#       다른 사람들 코드를 보니 내가 잘 모르는 방식이 많다. 비트연산자를 내가 제대로 공부한 적이 없어서 그런 듯 하다. 내일 따로 시간을 내서 꼼꼼히 공부하자