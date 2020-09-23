def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    return strings


# solution2
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))