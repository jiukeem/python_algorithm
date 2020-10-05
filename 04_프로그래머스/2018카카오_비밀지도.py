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


# 다른 사람의 solution
def solution(n, arr1, arr2):
    ans = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        ans.append(a12)

    return ans
# 내 코드와 이 코드 모두 O(n^2)인데 얘가 3배정도 빠르다. n 범위가 좁아서 정확한 평가는 아님
# 몰랐던 메소드는 rjust. 내가 첫번째, 두번째 포문으로 돌렸던 작업을 rjust 하나로 해결할 수 있다.
# rjust(width, fillchar) center과 ljust 도 있다
# replace의 경우는 알고 있었는데 bin(i|j)를 몰라서 활용을 못했다. 평소에 잘 안쓰던 메소드기도 했고.
# 이제 비트논리연산자를 보자.
bin(3)
>>> 0b11
bin(9)
>>> 0b1101
bin(3|9)
>>> 0b1011
# 신기하당. 십진수로는 생각하지 않고 이진수로 바꿔서 각 자리를 계산해주네. 하나라도 1이면 1
# 그럼 & and연산자는 둘 다 1이어야 1을 출력하는 식이구나.
# 음 그리고 bin의 결과값은 str 형식이다. 그럼 위의 코드에서 str 은 없어도 될 것 같은데?
# 테스트 해보니 맞다. 맨 첫줄에 str(bin())할 필요없이 bin()만 해도 결과는 같음
# 비트연산자 공부를 했다! 씬난다. int('1101' ,2) 식으로 int를 이용하는 방법도 다음에 써보자.