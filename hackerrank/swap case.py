text = input()

lst = []
for char in text:
    if char == char.lower():
        lst.append(char.upper())
    else:
        lst.append(char.lower())


result = ''.join(lst)
print(result)

#겁나 잘 짰는데 swapcase() 가 있었고요?ㅋㅋㅋ