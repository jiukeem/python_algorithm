from collections import deque

class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.terminal = None

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node.children.keys():
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.terminal = string

    def start_with(self, prefix):
        current_node = self.root
        ans = []

        for char in prefix:
            if char in current_node.children.keys():
                current_node = current_node.children[char]
            else:
                return None

        root_node = current_node
        queue = deque()
        queue.append(root_node)
        # 그래프가 아니라 트리형태니까 visited 프로퍼티는 없어도 괜찮을 것 같다.

        while queue:
            node_to_search = queue.popleft()
            if node_to_search.terminal:
                ans.append(node_to_search.terminal)
            for node in node_to_search.children.values():
                queue.append(node)

        return ans

    def search(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node.children.keys():
                return False
            current_node = current_node.children[char]

        return True if current_node.terminal else False

trie = Trie()
trie.insert('hello')
trie.insert('hell')
trie.insert('sunny')
trie.insert('sunshine')
trie.insert('swimming')
print(trie.start_with('sun'))
print(trie.start_with('s'))
print(trie.search('hell'))
print(trie.search('swim'))