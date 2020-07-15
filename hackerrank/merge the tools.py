text = input()
k = int(input())

'''lst = [text[i*k:(i+1)*k] for i in range(len(text)//k)]

for seg in lst:
    temp_lst = [i for i in list(seg)]
    text_new = ''
    for i in temp_lst:
        if i not in text_new:
            text_new += i
    print(text_new)
    
1차 답, 맞긴한데 더 깔끔하게 만들어보자
'''

lst = [text[i*k:(i+1)*k] for i in range(len(text)//k)]
print(lst)

# 포럼의 답들이 iter() 함수를 사용하는데 이게 뭔지 이해해야 코드를 줄일 수 있을 듯
