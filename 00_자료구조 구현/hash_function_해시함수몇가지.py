# 나누기 방법
def hash_function_remainder(key, array_size):
    return key % array_size
# 키가 40, 120, 788, 2307이고 배열의 크기를 200으로 설정한다고 하면
# 40, 120, 188, 107이 return된다.

# 곱셈 방법
def hash_function_multiplication(key, array_size, a):
    temp = a * key
    temp = temp - int(temp)

    return int(array_size * temp)
# 원리는 간단하다. a는 0에서 1사이의 값이고 요걸 key에 곱해준 뒤 소숫점만 취한다.
# 그럼 key마다 각자의 0에서 1사이 값을 가지겠죵
# 여기다가 배열의 크기를 곱하면 이 값들은 0에서 배열범위 안의 실수가 된다. 
# 이 실수에서 소수부분을 버리면 우리가 원하는 범위 내에서 자연수로 변환하기 성공
