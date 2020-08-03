# 내 답안
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 언제 str에서 list로 변환할건지. puctuation 제거 전? 후?
        # str 타입은 immutable 이므로 펑츄에이션 제거 + lower 하면서 바로 list로 만들어주는 것이 좋겠다.

        # 클리닝작업
        cleaned_paragraph = re.sub(r'[^\w]', ' ', paragraph)
        # 토큰화 (단어들 리스트로 생성)
        words = [word for word in cleaned_paragraph.lower().split() if word not in banned]

        # 빈도수 딕셔너리 생성
        counts = {}
        for word in words:
            if word not in counts.keys():
                counts[word] = 1
            else:
                counts[word] += 1

        # 빈도수로 정렬
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        return sorted_counts[0][0]
        # 첫번째 튜플의 0번째 인덱스 출력
# 람다펑션이 굉장히 유용하구나.
# sort()는 원본 리스트를 변경하고 아무것도 return하지 않는다 (None)
# sorted()는 원본에 영향을 주지 않고 새로운 객체를 반환하며 모든 iterable 에 동작한다.
# 문자열도 사용가능하긴 한데 결과값이 문자열이 아닌 글자당 리스트로 나오는 것에 유의
# sort는 list에 속한 함수, 즉 메소드이므로 .sort()로 사용하고 sorted는 sorted(iterable)로 사용한다.
# 메소드와 함수의 차이, 좀 더 공부하기
# runtime은 상위 30프로, 메모리사용량은 상위 10프로! 넘모 뿌듯ㅜㅜ



# 교재의 방식: Counter 객체 사용
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
# Counter는 파이썬에서 제공하는, 딕셔너리와 관련된 특수한 형태의 자료형이라고 한다.
# a = [1, 2, 3, 4, 5, 5, 5, 6, 6] 일 때,
# b = collections.Counter(a)
# b를 출력하면 Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1}) 로 딕셔너리를 만들어준다.
# most_common 메소드를 이용해서 빈도수가 높은 애들을 리스트로 받아볼 수 있다.
# 즉, b.most_common(2) 은 [(5, 3), (6, 2)]를 return 한다

