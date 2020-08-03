num_of_input = int(input())
num_lst = list(map(int, input().split()))

biggest_value = num_lst[0]
smallest_value = num_lst[0]

for i in num_lst:
    if biggest_value < i:
        biggest_value = i
    if smallest_value > i:
        smallest_value = i

print(smallest_value, biggest_value)

#간단히 이렇게도 가능
print(min(num_lst), max(num_lst))