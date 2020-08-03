N, X = map(int, input().split())
A = list(input().split())

smaller_lst = []
for i in A:
    if int(i) < X:
        smaller_lst.append(i)

print(' '.join(smaller_lst))
