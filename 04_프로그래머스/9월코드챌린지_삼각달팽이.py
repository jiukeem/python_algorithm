def solution(n):
    fin = sum(range(1, n + 1))
    mat = [[0] * i for i in range(1, n + 1)]

    m = 1
    chg = 0
    while True:
        i = 0 + chg * 2
        j = 0 + chg
        while i < n and mat[i][j] == 0:
            mat[i][j] = m
            i += 1
            m += 1

        k = n - 1 - chg
        g = 1 + chg
        while g < len(mat[k]) and mat[k][g] == 0:
            mat[k][g] = m
            g += 1
            m += 1

        x = n - 2 - chg
        y = -1 - chg
        while 0 < x and mat[x][y] == 0:
            mat[x][y] = m
            x -= 1
            m += 1

        chg += 1
        if fin < m:
            break

    ans = []
    for lst in mat:
        ans += lst
    return ans
# Status: Accepted
# Note: 이렇게 의미없는 변수가 많아질 때 이름 설정을 어떻게 해야할지 잘 모르겠다.
#       다른 사람들 코드를 보니 i, j의 두 개로 해결할 수 있다.
#       mode 변수를 써서 # 0 : go down, 1 : go right, 2 : go up 이라고 코멘트를 달아놓으니 보는 사람이 이해하기가 쉽다.
#       방법은 맞았지만 좀 더 깔끔하고 처음보는 사람이 이해하기 쉽도록 다시 짜보자.


def solution(n):
    mat = [[0] * i for i in range(1, n + 1)]
    step, cnt, i, j = n, 1, -1, 0
    mode = 0 # 0: down, 1: left to right, 2: up
    while True:
        for _ in range(step):
            if mode %3 == 0:
                i += 1
            elif mode %3 == 1:
                j += 1
            else:
                i -= 1
                j -= 1
            mat[i][j] = cnt
            cnt += 1
        mode += 1
        step -= 1
        if step < 1:
            break

    ans = []
    for row in mat:
        ans += row
    return ans
# Status: Accepted
# Note: 마지막 숫자에 도달하면 break 하는 것보다 step 을 사용하는게 훨씬 더 간결하다.
