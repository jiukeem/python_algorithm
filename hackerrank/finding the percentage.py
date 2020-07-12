dict = {}
for _ in range(int(input())):
    text = input().split()
    name = text[0]
    score = [int(a) for a in text[1:]]
    dict[name] = score

quora = input()
print(dict)
print(quora)

for name in dict:
    if name == quora:
        
