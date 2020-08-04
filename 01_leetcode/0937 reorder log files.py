class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums, letters = [], []
        for log in logs:
            if log.split()[1].isdigit():
                nums.append(log)
            else:
                letters.append(log)
                # 현재 숫자든 레터든 전부 문자열 타입(str)으로 들어와있다.
                # isdigit은 해당 문자열이 숫자로 변환 가능한지 확인해주는 함수
                # 마찬가지로 isalpha도 사용가능하다. True/False로 결과값이 나온다.
                # 역시 있을거라고 추측하는 함수는 파이썬에 다 있다.
                # 둘다 str 타입에 사용하는 함수임 헷갈리지 말기~

        # nums는 더이상 건드릴 것 없이 정렬한 letters 뒤에 붙여주면 된다.

        letters.sort(key=(lambda x: (x.split()[1:], x.split()[0])))
        # 람다는 a = lambda x: (x*2) + 3
        # a(5) = 13처럼 함수 선언없이 간단히 한줄로 펑션을 define한다.
        # sort의 key perameter에 원래 letters의 요소들(x)이 차례로 들어갈텐데,
        # 이 때 람다펑션이 발동해서 x의 두번째 요소를 키의 argument로 넣어준다.
        # 뒤에 x.split()[0]은 앞의 key가 동일한 경우 0번째, 즉 아이덴티파이어를 비교하라는 뜻
        # 나 혼자서는 요 부분 못짰을거다.

        ordered_logs = letters + nums
        return ordered_logs




