num = int(input())
text = input()

lst = [int(i) for i in text.split()]
tpl = tuple(lst)
print(hash(tpl))