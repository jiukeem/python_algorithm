def solution(s):
    s = s.lower()
    p, y = 0, 0
    for char in s:
        if char == 'p':
            p += 1
        if char == 'y':
            y += 1

    return p == y