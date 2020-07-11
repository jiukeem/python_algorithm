for _ in range(int(input())):
    name = input()
    score = float(input())
    dict = {}
    dict[name] = score

''' 
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
'''

scores = list(dict.values())
scores = scores.sort()
print(scores)