def solution(numbers):
    ans = set()
    for i, n_1 in enumerate(numbers):
        for n_2 in numbers[i + 1:]:
            ans.add(n_1 + n_2)

    return sorted(list(ans))
