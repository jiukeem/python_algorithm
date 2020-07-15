word = input()
vowel = ['A', 'E', 'I', 'O', 'U']

vowel_count = 0
cons_count = 0
for i in range(len(word)):
    if word[i] in vowel:
        vowel_count += len(word) - i
    else:
        cons_count += len(word) - i

if cons_count > vowel_count:
    print('Stuart', cons_count)
elif cons_count < vowel_count:
    print('Kevin', vowel_count)
else: print('Draw')
