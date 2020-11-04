# coding=utf-8

# my solution
def solution(numbers):
    ans = ''.join(sorted(map(str, numbers), key=lambda x: x * 3, reverse=True))
    return str(int(ans))
# Status: Accepted
# Intuition: sort by str data type
# Note: 처음에는 오름차순 정렬시킨 다음에 두자리수가 등장하는 인덱스, 세자리수가 등장하는 인덱스를 찾는 방식으로 구현하고 있었는데
#       너무 심하게 복잡해져서 이 난이도가 이렇게 어려울리 없는데? 하다가 문득 str 타입인 상태로 정렬시키면 될 것 같은 예감에 테스트를 해봤다.
#       그랬더니 내가 원하는대로 앞자리수부터 비교하여 정렬해주더라! 넘나 기쁨쓰
#       즉 int 로 하면 10, 6, 2 순으로 정렬되고 str 으로 하면 6, 2, 10 이렇게 내가 원하는 식으로 나온다.
#       하나 더 해결해야 하는 문제는 31과 3이 있을 때 31, 3 순으로 정렬이 되어버린다는 것.
#       join 했을 때 313보다 331이 더 크기 때문에 이런식으로 정렬이 이루어지면 곤란했다. 그 부분은 key 를 사용해서 해결했다. 숫자의 범위가 세자리 수이기 때문에 *3을 해줬다.
#       마지막에 int 로 변경했다가 다시 str 해주는 건 다른 사람들의 질문글을 참고해서 알아낸건데 처음에는 저 부분없이 제출했더니 딱 한 개의 tc에서만 실패가 떴다.
#       예외 케이스로 모든 숫자가 0일 때 0000이 아니라 0이 출력되어야 하기 때문에 저런 변환 과정이 한번 더 필요했던 것.
#       예외 케이스를 못 떠올리긴 했지만 그래도 풀이 방법이나 *3 을 key로 사용하는 건 내가 해결했으니 왕 뿌듯하당.
#       이게 가장 인기있는 답안이긴 했는데 두번째 답안도 좋아보여서 공부해두면 좋을 것 같다.


# 다른사람의 풀이
import functools

def comparator(a, b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    ans = str(int(''.join(n)))
    return ans
# 음 다른 부분은 사실 내 풀이와 원리가 같고 key 부분이 관건인데 cmp_to_key가 뭐지?
# 오잉 찾아보니 cmp는 파이썬 2.x 버전에서 람다 대신 사용했던 매개변수라고 한다.
# 람다랑 사실상 같은 원리이고 함수를 따로 구현한뒤 key 파라미터로 넘겨주고 싶을 때 functools.cmp_to_key(함수명)을 쓸 수 있다.
# 그럼 저 함수의 용도는 이해했고 이제 comparator를 보자.
# comparator는 두개의 str을 인자로 받고 있다. 흠 두 개인게 람다와 좀 다른 부분인데,
# 약간 greedy의 느낌인 것 같다. 지금 이 요소가 a 가 되고 비교해야 할 다른 요소가 b가 된다.
# 두 요소를 두가지 순서로 더해본 뒤, 지금 요소가 앞에 있는게 더 크면(즉, t1이 더 크면) 1이 return 되고 아니면 -1이 return 된다.
# 흠 이게 key가 음수면 두 요소의 자리가 바뀌고 양수면 유지되는거 같은데? 그리고 이 key 값은 두 요소를 비교할 때만 사용하고
# 다른 요소와 비교하는 단계로 넘어갈 때는 폐기되고 다시 계산되어지는 것 같다.
# 찾아봐도 cmp_to_key 에 대한 정보가 별로 없당.

