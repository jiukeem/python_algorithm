lst = []
for _ in range(int(input())):
    lst.append([input(), float(input())])

print(lst)

second_lowest = sorted(list(set([score for name, score in lst])))[1]
print(second_lowest)
result = [name for name, score in sorted(lst) if score == second_lowest]
print('\n'.join(result))

# 답지 보고 했다. 어렵다잉 모르는 기능은 없는데!
# 다음 문제부터는 아무리 코드가 지저분해지더라도 일단 내 답을 낸 다음에 답지를 보자

'''dict = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    dict[name] = score


_ 는 for문 안에서 _를 쓸 일이 없을 때 사용하는 듯 하다.
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
이렇게 input을 받을 건데 range(5) 가 되니까 다섯번 반복하라는 얘기지. i 랑 사실상 똑같지만
실행 내용에 i 가 등장하지 않을 때 _를 사용하는 것 같다.
아 근데 저렇게 하면 name 과 score 이 계속 다음 input으로 교체되는 거 아닌가?
내가 딕셔너리에 key: value 로 넣어줘야하나보다
그럼 이런식으로 나온다
[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 아, 딕셔너리가 아니라 리스트로 받는게 더 낫나?
내가 만든건
{'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41, 'Harsh': 39}


print(dict)
scores = list(dict.values())
print(scores)
scores.sort() #sort는 원래의 리스트를 변형하기 때문에 new_score = scores.sort() print(new_score) 하면 None 이 나온다.
print(scores)
a = set(scores)
minimum = min(a)
print(min(a))
second = min(a.pop(minimum))
print(second)
계속 너무 복잡해지기만 하네 ㅜㅜ 다른 방법을 생각해보자'''

