# my solution
def solution(n, lost, reserve):
    new_lost = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)

    lost_num = len(new_lost)
    for i in new_lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            lost_num -= 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            lost_num -= 1

    return n - lost_num
# Status: Accepted
# Note: 되게 수정을 많이 했다.
#       처음에는 new_lost나 lost_num 사용없이 lost.remove(i)를 썼는데 지금 포문 돌리는 중인 리스트에 변형을 가하니까 문제가 생긴듯 하다.
#       그리고 처음에는 한개의 for 문으로 합했었는데 그렇게 하니까 오류가 나는 tc들이 있었다.
#       lost와 reserve 둘 다에 들어있는 넘버들을 먼저 다 처리해줘야 제대로 돌아간다.
#       흠 근데 lost.remove 를 썼을 때 new_lost나 lost_num 의 새로운 변수를 안만들어도 돼서 엄청 깔끔했는데.. 다른 사람들 풀이를 한번 보자.


# 다른 사람의 solution
def solution(n, lost, reserve):
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]

    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1)
        elif r + 1 in _lost:
            _lost.remove(r + 1)

    return n - len(_lost)
# 너무 깔끔해서 기분이 좋다. 일단 배우고 싶은 부분은 _lost 와 _reserve 를 만드는 코드. 너무 깔쌈해서 기분이 좋다.
# 두번째는 _lost.remove 를 쓸거니 포문을 _lost 가 아닌 _reserve로 돌리는 것.
# 이거 O(n^2)가 보다 작게 만들 수 있나? remove가 깔끔하긴 하지만 효율적인 연산은 아닌데.