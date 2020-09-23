# my solutioin
import re

def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False

    m = re.search(r'\D', s)
    return m == None
# Status: Accepted
# Note: 정규표현식을 써봤다. 잘쓰는 사람을 보면 len까지 체크하던데 나도 좀 더 연마해야겠당


# 다른 사람의 solution
def solution(s):
    return s.isdigit() and len(s) in (4, 6)
# isdigit()을 생각못했당 아주 깔끔한 코드

# 다른 사람의 solution
def solution(s):
    return bool(re.match("^(\d{4}|\d{6})$", s))
# Note: 아 생각보다 어렵지 않네, digit이 4번반복되거나 6번반복되는 경우가 있는지 체크체크하는 방식


# isdecimal isdigit isnumeric 은 모두 간단히 말해 숫자인지를 체크해주지만
# isdecimal은 0-9 사이의 열가지만 인정하고
# isdigit 은 3^2(위첨자 형식의 2) 로 써있어도 인정하고
# isnumeric은 1/2(가 한글자로 되어있는 특수문자) 의 경우도 인정한다.