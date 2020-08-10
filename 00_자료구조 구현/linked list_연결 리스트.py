# 연결리스트 개념을 제대로 이해하기 위해 파이썬으로 구현해보기로 함

# 노드 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)       # 얘는 출력용

head = Node(5)
next_node = Node(12)
head.next = next_node
# 이런 식으로 포인터 구현. 5의 다음 값은 12가 된다
# .next를 통해 간단히 다음 노드로 이동할 수 있다.

#단순 연결리스트
class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    # 첫번째 노드 삽입하기
    def insertFirst(self, data):
        new_node = Node(data)       # 새로운 노드 생성
        temp_node = self.head       # 기존의 first 노드를 잠시 보관
        self.head = new_node        # 연결리스트의 head를 새로운 노드로 변경
        self.head.next = temp_node  # 새 head의 링크(포인터)를 기존 head로 지정

        self.list_size += 1

    # 인덱스로 노드 선택하기
    # 원래 연결리스트는 자료 번호 없이 관계만 있어서 특정 값만 불러내오기 어려움
    def selectNode(self, num):
        if self.list_size < num:
            return                  # 내가 부르려는 인덱스가 리스트 사이즈보다 큰 경우
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node                 # 카운트를 하나씩 늘리면서 .next로 다음 노드로 넘어가고
                                    # count와 num이 같아지는 순간 연산 종료 및 노드 return

    # 중간에 노드 삽입하기
    def insertMiddle(self, num, data):
        if self.head.next == None:  # 값이 head 하나 밖에 없는 경우
            self.insertLast(data)

        node = self.selectNode(num) # 기존의 num 인덱스에 위치한 node 불러오기
        new_node = Node(data)       # 새로운 노드 생성
        self.selectNode(num-1).next = new_node
        new_node.next = node        # num 앞 노드의 링크 수정 및 새 노드의 링크를 기존 num으로 지정

        self.list_size += 1

    # 마지막에 노드 삽입하기
    def insertLast(self, data):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next        # 마지막 노드로 이동

        new_node = Node(data)
        node.next = new_node        # 노드 추가 및 기존 마지막 노드의 링크 연결

        self.list_size += 1

    # 노드 삭제하기
    def deleteNode(self, num):
        if self.list_size <= num:
            return
        if num == 0:
            self.deleteHead()
            return

        node = self.selectNode(num-1)
        del_node = node.next
        node.next = node.next.next  # 삭제할 노드 앞 노드의 링크 수정
        del del_node                # 노드 삭제

        self.list_size -= 1

    # 첫번째 노드 삭제하기
    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

        self.list_size -= 1

    # 마지막 노드 삭제하기
    def deleteLast(self):
        node = self.selectNode(self.list_size - 2)
        last_node = node.next
        node.next = Nonde
        del last_node

        self.list_size -= 1

    # 출력테스트용
    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node.next == None:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list


if __name__ == "__main__":
    m_list = SingleLinkedList(1)
    m_list.insertLast(5)
    m_list.insertLast(6)
    print('LinkedList :', m_list)
    print('LinkedList Size() :', m_list.list_size)
    print('LinkedList SelectNode(1) :', m_list.selectNode(1))

    m_list.insertMiddle(1, 15)
    print('LinkedList Insert Middle(1, 15) :', m_list)

    m_list.insertFirst(100)
    print('LinkedList Insert First(100) : ', m_list)
    print('LinkedList SelectNode(0) :', m_list.selectNode(0))

    m_list.deleteNode(0)
    print('LinkedList Delete Node(0) : ', m_list)
    m_list.deleteHead()
    print('LinkedList Delete Head : ', m_list)
    m_list.deleteNode(1)
    print('LinkedList Delete Node(1) : ', m_list)











