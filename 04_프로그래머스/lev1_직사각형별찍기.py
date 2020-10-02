# my solution
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*'*a)
# Status: Accepted
# Note: ('*' * a + '\n') * b 는 마지막에 공백한줄이 추가된다.