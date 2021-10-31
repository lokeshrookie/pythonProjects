class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data : %s>" % self.data


class LinkedList:
    """
    Singly LInkedLIst
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.next_node
        return count


#  Condole History
# """
# Console Work 1---------
# n = LinkedList()
# n.N1 = Node(10)
# print(n.size())
# 0
# n.N2 = Node(20)
# n.N1.next_node = n.N2
# print(n.size())
# 0
# n.head = n.N1
# print(n.size())
# 2
# """
# """n1 = LinkedList()
# n1.is_empty()
# Out[5]: True
# n1.size()
# print(n1.size())
# None
# n1.append(5)
# Traceback (most recent call last):
#   File "C:\Users\loki\AppData\Roaming\Python\Python39\site-packages\IPython\core\interactiveshell.py", line 3441, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-8-b57fded54b85>", line 1, in <module>
#     n1.append(5)
# AttributeError: 'LinkedList' object has no attribute 'append'
# N1 = Node(10)
# N2 = Node(20)
# n1.head
# print
# Out[12]: <function print>
# print(n1)
# <__main__.LinkedList object at 0x000001B581FA6370>
# print(n1.size())
# None
# N1.next_node = N2
# print(n1.is_empty())
# True
# n1.N1 = Node(10)
# n1.N2 = Node(20)
# print(n1.is_empty())
# True
# n1.head
# n1.head = N1
# print(n1.is_empty())
# False
# print(n1)
# <__main__.LinkedList object at 0x000001B581FA6370>
# print(n1.N1)
# <Node data : 10>
# n1.N1.__hash__()
# Out[25]: 117442574249
# print(n1.size())
# None
# """
