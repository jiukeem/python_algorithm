'''
orig_num = input()

if len(orig_num) == 1:
    orig_num = '0' + orig_num

calculated_num = 0
num = orig_num
result = 0
cycle = 0
while result != orig_num:
    calculated_num = int(num[0]) + int(num[-1])
    num = num[-1] + str(calculated_num)[-1]
    result = num
    if len(result) == 1:
        result = '0' + result
    cycle += 1

print(cycle)
'''

#while True 와 str 사용없이 해보기

orig_num = int(input())

cycle = 0
num = orig_num
while True:
    a = int(num/10)
    b = num%10
    c = a + b
    num = b*10 + c%10
    cycle += 1
    if num == orig_num:
        print(cycle)
        break


