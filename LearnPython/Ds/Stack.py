
class Stack:
    # constructor initialisation
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def is_empty(self):
        # return len(self.stack) <= 0
        return self.stack == []

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        # if len(self.stack) > 0:
        #     return self.stack[len(self.stack)-1]
        # else:
        #     return None

    def get_stack(self):
        return self.stack




# Object of Stack class created and named as obj

obj = Stack()
# obj.push(5)
# # obj.is_empty()
# # print(obj.is_empty())
# # obj.push(6)
# obj.push(7)
# obj.push(8)
# obj.push(9)
#
#
# print(obj.pop())
print(obj.peek())
# print(obj.get_stack())
