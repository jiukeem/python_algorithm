x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n]
print(result)

'''result = [[a, b, c] for a, b, c in range(x+1), range(y+1), range(z+1) if a + b + c != n]
print(result)
'''
# key, value 처럼 쌍으로 가져오는게 아니라 a 마다 모든 b 반복 식으로 진행되야 하기 때문에 for 문을 각각 써줘야 한다.