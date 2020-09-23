# my solution 1
def solution(s, n):
    ans = ''
    for char in s:
        if char == ' ':
            ans += char
        else:
            asc = ord(char)
            if 64 < asc < 91:
                new_asc = asc + n
                if new_asc > 90:
                    new_asc -= 26
                ans += chr(new_asc)
            if 96 < asc < 123:
                new_asc = asc + n
                if new_asc > 122:
                    new_asc -= 26
                ans += chr(new_asc)

    return ans
# Status: Accepted
# Note: 아스키코드를 처음 사용해봤다. 지금 코드가 굉장히 덕지덕지 지저분한데 일단 처음 써보는거니까..
#       물론 아스키코드가 아니더라도 그냥 참조 스트링을 만들어서 더 간단하게 할 수 있을듯 하다.


# my solution 2
def solution(s, n):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    # lower = upper.lower() 로 할수도 있지만 읽기 쉽게

    ans = ''
    for char in s:
        if char == ' ':
            ans += char
        elif char in upper:
            ans += upper[(upper.index(char) + n) % 26]
        elif char in lower:
            ans += lower[(lower.index(char) + n) % 26]

    return ans
# Status: Accepted
# Note: 아스키코드 변환보다 좀 더 읽기 쉽지만 인덱스를 구한 뒤 n을 더해서 다시 인덱싱하는게 조금 별로다


# my solution 3 (다른 사람의 풀이 참조)
def solution(s, n):
    ans = ''
    for char in s:
        if char.isupper():
            ans += chr((ord(char) - ord('A') + n)%26 + ord('A'))
        elif char.islower():
            ans += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:
            ans += ' '

        return ans
# Status: Accepted
# Note: 아스키코드를 쓰지만 isupper/islower을 사용하고 범위설정도 더 간결하게 바꿨다.
#       그리고 아스키코드 표를 참조하지 않아도 - ord('A') 를 쓰는 식으로 풀 수 있다.
