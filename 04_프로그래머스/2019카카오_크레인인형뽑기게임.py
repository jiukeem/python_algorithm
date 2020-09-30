# my solution
def solution(board, moves):
    stack = []
    ans = 0
    for m in moves:
        # 0이 아닌 지점 찾기
        row = 0
        while row < len(board) and board[row][m - 1] == 0:
            row += 1

        # row == len(board)면 해당 위치에는 집을 인형이 없다는 뜻이므로 pass
        if row != len(board):
            if stack:
                last = stack[-1]
            else:
                last = None
            stack.append(board[row][m - 1])

            # 같은 인형 두개가 연속한 경우 팡팡
            if last and stack[-1] == last:
                stack.pop()
                stack.pop()
                ans += 2

            # 집은 인형이 있던 자리는 0으로 변경
            board[row][m - 1] = 0

    return ans
# Status: Accepted
# Note: 노트를 달지 않으면 이해하기가 어려울 것 같다. 지금은 달아놔서 각 부분 코드가 뭐하는지 알 수 있지만..
#       코드를 잘 짜게 되면 코멘트 없이도 한눈에 작업 방식/순서가 한 눈에 들어올까?


# 다른 사람의 solution
def solution(board, moves):
    stack = []
    ans = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        ans += 2

                break

    return ans
# Note: 아, 훨씬 잘읽힌다. 내 코드는 row를 찾는부분, 같은 인형 두개가 연속되어 있는지 확인하는 부분 등
#       부분집합들로 구성되어 있는데 얘는 하나의 큰 덩어리 같은 느낌이다. 훨씬 읽기 쉽다.
#       나는 if문, for문 은 중첩되지 않게 만드는게 제일 중요하다고 생각했는데 이 코드를 보면 전혀 그렇지 않다.
#       break이 있어서 더 오래걸리는 것도 아니고 무엇보다 읽기가 너무 쉽다.
#       마지막 break의 위치를 찾는 데에 좀 헤맸는데 break은 점점 바깥으로 나가면서 가장 먼저 만나는 반복문을 break 시키는 건가?
#       if 문 안에 들어있는게 좀 어색하게 느껴졌다.