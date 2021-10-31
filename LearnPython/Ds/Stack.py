
class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "there is no elements"

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

# Object of Stack class created and named as obj
obj = Stack()
obj.push(6)
obj.push(7)
obj.push(8)
obj.push(9)


print(obj.pop())
print(obj.peek())
