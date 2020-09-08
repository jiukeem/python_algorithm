# my solution
def solution(phone_book):
    if len(phone_book) == 1:
        return False
    for i, num1 in enumerate(phone_book):
        for num2 in phone_book[i+1:]:
            if num1 == num2 or num1 == num2[:len(num1)] or num2 == num1[:len(num2)]:
                return False
    return True
# Status: Accepted
# Algorithm: Brute Force
# Time Complexity: O(n^2)

# 다른 사람의 코드
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True
# 이게 더 직관적인데 시간이 훨씬 많이 소요된다 왜지?
# sorted는 아마 O(n lg(n))일테니 startswith 함수가 오래걸리나보다.