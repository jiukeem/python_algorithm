# my solution
def solution(skill, skill_trees):
    ans = [None] * len(skill_trees)

    for idx, s in enumerate(skill_trees):
        series = list(skill) # series = skill 도 가능
        for char in s:
            # 비교할 스킬트리가 남아있지 않다면 작업 중단하고 True 값 지정
            if not series:
                ans[idx] = True
                break

            # 스킬트리의 첫번째에 해당할 경우 스킬트리의 맨 앞을 지우고 계속 진행
            if char == series[0]:
                series = series[1:]

            # 스킬트리의 첫번째가 아닌 요소와 일치한다면 작업 중단하고 False 값 지정
            if char in series[1:]:
                ans[idx] = False
                break
        else:
            ans[idx] = True

    return sum(ans)
# Status: Accepted
# Note: for-else 문을 썼다. 저번에 공부한걸 스스로 떠올려서 쓰다니 기특하당ㅎㅎ
#       총 갯수만 return하면 되므로 ans를 [None] * len 대신 그냥 0으로 하면 더 간단해질 것 같다. ans[idx] = False를 생략할 수 있음


# 다른사람의 solution
def solution(skill, skill_trees):
    ans = 0

    for s in skill_trees:
        series = list(skill)

        for char in s:
            if char in series:
                if char != series.pop(0):
                    break
        else:
            ans += 1

    return ans
# Status: Accepted
# Note: 원리는 같다. 근데 내 코드보다 더 나은 부분은,
#       내 코드의 두번째 세번째 이프문을 하나로 통합한 것: if char in series 로 묶었다.
#       pop(0)을 사용한 것. 이러면 char == [0] 일 경우에 따로 추가 작업을 해주지 않아도 된다.
#       똑똑하고 간결한 방법.