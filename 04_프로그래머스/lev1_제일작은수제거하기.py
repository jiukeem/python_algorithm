# my solution
def solution(arr):
    if len(arr) == 1:
        return [-1]

    arr.remove(min(arr))
    return arr
# Status: Accepted


def solution(arr):
    return [i for i in arr if i > min(arr)] or [-1]
# 이게 더 깔끔한 코드라고 생각했는데 위 코드보다 시간이 훨씬 오래걸린다(심지어 타임아웃)
# 위 코드는 min에서 O(n) remove에서 O(n)이므로 O(n)이다.
# 이 코드도 O(n)인 것 같은데? 설마 리스트 컴프리헨션에서 min을 매번 계산하나? 그럼 O(n^2)이겠다.
# 다만 이 코드는 arr안에 min 값의 원소가 여러개일 때 해결할 수 있다.
# 물론 이 문제에서는 제한조건에 i != j 일때 arr[i] != arr[j] 라고 명시했기 때문에 위 코드도 상관없다.