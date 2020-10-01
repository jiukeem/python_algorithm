def solution(n, m):
    ans = []
    for i in range(min(n, m) + 1, 0, -1):
        if n % i == 0 and m % i == 0:
            ans.append(i)
            break

    for i in range(max(n, m), n * m + 1):
        if i % n == 0 and i % m == 0:
            ans.append(i)
            break

    return ans
# Status: Accepted
# Note: 코드는 간단하고 예외가 없이 항상 답을 찾아내긴 하지만 너무 비효율적인 것 같다.


# 구글링 해보니 가장 최대공약수(GCD)와 최소공배수(LCM)에 관한 가장 효율적인 알고리즘이 있다
# 유클리드 호제법 - 증명은 생각보다 어렵지 않으니 까먹으면 한번씩 찾아볼 것
# 반복문 혹은 재귀로 가능한데, 이 알고리즘의 경우 재귀를 쓰면 마법같아 보인다. 너무 간단해
def GCD(n, m):
    min_num, max_num = min(n, m), max(n, m)
    if max_num % min_num == 0:
        return min_num
    else:
        return GCD(min_num, max_num % min_num)

# 만약 n < m이라는 조건이 주어진다면 더 간단하다.
def GDC(n, m):
    r = m % n
    if r == 0:
        return n
    else:
        return GCD(n, r)

# 또한 최소공배수는 n * m / 최대공약수로 구할 수 있다.
# 이 문제의 경우는 GCD와 LCM을 리스트에 담아서 return 해야하므로 재귀보다는 반복문이 적절할 것 같다.
def solution(n, m):
    x, y = max(n, m), min(n, m)
    r = x % y
    while 0 < r:
        r, y = y % r, r

    gcd = y
    lcm = n * m // y #int 형식으로 나와야 하기 때문에
    return [gcd, lcm]
# Status: Accepted
# Note: 프로그래머스는 정확한 연산시간은 안알려주지만 맨 위의 코드는 tc 중 최대 48ms까지 나온 반면
#       이 코드는 최대 값이 0.1ms 이다!
#       위의 코드는 시간복잡도 O(n*m)이고, 유클리드 호제법을 이용한 이 풀이는 O(log(n+m))이다. 엄청난차이!

