import numpy as np

X = np.array([[51, 55],[14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])

X = X.flatten()
print(X)

print(X[np.array([0, 2, 4])])
print(X[0], X[2], X[4])
print(np.array([X[0], X[2], X[4]]))
print(X[[0, 2, 4]])


print(X > 15)
print(X[X>15])

list = [51, 55, 14, 19, 0, 4]
print(list > 15)
# 리스트는 이렇게 활용할 수 없음! 넘파이 어레이만 가능 ~.~