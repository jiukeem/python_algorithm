a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

whole_score = [a, b, c, d]
whole_result = []

for score in whole_score:
    sum_of_victory = 0
    sum_of_defeat = 0
    sum_of_tie = 0
    count_of_tie_team = 0
    sum_of_each_team_score = 0

    for i in range(6):
        sum_of_victory += score[3*i]
        sum_of_defeat += score[3*i + 2]
        sum_of_tie += score[3*i + 1]
        if score[3*i + 1] != 0:
            count_of_tie_team += 1

    if sum_of_defeat == sum_of_victory and sum_of_tie % 2 == 0 and sum_of_victory + (sum_of_tie/2) == 15 and count_of_tie_team!= 1:
        whole_result.append(1)
    else:
        whole_result.append(0)

print(' '.join(map(str, whole_result)))\
