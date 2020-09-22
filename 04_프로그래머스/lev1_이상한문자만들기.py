def solution(s):
    words = s.split(' ')
    ans = []
    for w in words:
        new_w = ''
        for i, char in enumerate(w):
            if i % 2 == 0:
                new_w += char.upper()
            else:
                new_w += char.lower()
        ans.append(new_w)

    return ' '.join(ans)

