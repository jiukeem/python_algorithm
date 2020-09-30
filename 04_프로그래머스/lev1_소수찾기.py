def solution(n):
    ans = 1
    for i in range(3, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans += 1

    return ans
# 시간복잡도는 그렇다치고, else가 저 자리에 있는데 왜 에러가 안나는거지?
# else 없이 ans += 1 을 하면 j에 관한 포문 결과에 상관없이 결국 모든 i들에 대해 작동하게 돼서 문제가 생긴다.
# 흠, break과 else의 관계에 대해서 좀 찾아봐야겠다.
# 이 게시글이 이해하기 쉽다. https://kongdols-room.tistory.com/42
# if문이 아니라 while문과 for문에도 else를 사용할 수 있구나. 저 else는 for j 에 따라오는 절이며, for문이 종료되는 시점에 else 절의 내용을 실행한다.
# for문에 포함된 절이므로 break으로 for문을 깨고 나오는 경우, else 절은 실행되지 않는다 -> 이걸 이용한거네!

# 어쨌든 이 풀이는 시간초과가 난다. 더 줄일 방법을 생각해보자