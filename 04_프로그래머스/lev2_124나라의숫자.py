# my solution
def solution(n):
    table = {
        '0': '1',
        '1': '2',
        '2': '4'
    }

    temary = ''
    i, j = n // 3, n % 3
    while 0 < i:
        temary += str(j)
        i, j = i // 3, i % 3
    temary += str(j)

    ans = ''
    for s in temary[::-1]:
        ans += table[s]

    return int(ans)
# Status: Wrong Answer
# Intuition: 생각한 방법은 숫자가 3개밖에 못쓰이니 결국 3진수랑 다름이 없고 출력할 때만 0 -> 1, 1-> 2, 2 -> 4 로 바꾸면 될거라는 아이디어
#            우선 3진수 구현을 성공적으로 한 건 칭찬해주고 싶당. bin() 이나 int( , ) 등 기존함수가 아니라 직접 구현해본건 처음인데 돌려보니 잘 돌아간다.
#            while문이 끝난 뒤에 j를 한번 더 더해야하는 군더더기는 맘에 안들지만 어쨌든 성공
#            근데 애초에 이 방법은 틀린 방법이더라. 직접 구해보면 3, 6, 9 등 자릿수가 넘어가는 부분에서 3진수와 124나라의 숫자는 서로 달라진다. 
#            이 나라가 그지같다. 0은 표현안할거여? 0을 1이라고 표현해야하는데 1 -> 1 부터 시작하니 아구가 안맞는당. 다른 방법을 생각해야 할 것 같다.


# 번외) 재귀함수로 10진수를 n진수로 변환하기
def convert(number, n):
    i, j = divmod(number, n)
    if i == 0:
        return str(j)
    return convert(i, n) + str(j)
# 재귀짱


