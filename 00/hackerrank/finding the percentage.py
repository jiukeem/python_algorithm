dict = {}
for _ in range(int(input())):
    text = input().split()
    name = text[0]
    score = [float(a) for a in text[1:]]
    dict[name] = score

quora = input()
print(dict)
print(quora)

for name in dict.keys():
    if name == quora:
        result = sum(dict[name]) / len(dict[name])

print('%.2f'% result)

# 히히 잘짜서 기분좋다
        
