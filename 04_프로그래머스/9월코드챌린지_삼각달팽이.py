def solution(n):
    fin = sum(range(1, n + 1))
    ans = [[0] * i for i in range(1, n + 1)]

    m = 1
    chg = 0
    while True:
        i = 0 + chg * 2
        j = 0 + chg
        while i < n and ans[i][j] == 0:
            ans[i][j] = m
            i += 1
            m += 1

        k = n - 1 - chg
        g = 1 + chg
        while g < len(ans[k]) and ans[k][g] == 0:
            ans[k][g] = m
            g += 1
            m += 1

        x = n - 2 - chg
        y = -1 - chg
        while 0 < x and ans[x][y] == 0:
            ans[x][y] = m
            x -= 1
            m += 1

        chg += 1
        if fin < m:
            break

    output = []
    for lst in ans:
        output += lst
    return output
# Status: Accepted
# Note: 이렇게 의미없는 변수가 많아질 때 이름 설정을 어떻게 해야할지 잘 모르겠다.
#       다른 사람들 코드를 보니 i, j의 두 개로 해결할 수 있다.
#       mode 변수를 써서 # 0 : go down, 1 : go right, 2 : go up 이라고 코멘트를 달아놓으니 보는 사람이 이해하기가 쉽다.
#       방법은 맞았지만 좀 더 깔끔하고 처음보는 사람이 이해하기 쉽도록 다시 짜보자.