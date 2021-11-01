class Stack2(object):

    #constructor initialisation
    def __init__(self):
        self.stack = []
        self.numofitems = 0

    def isEmpty(self):
        return self.stack == []

    # Insert will
    def push(self, item):
        self.stack.insert(self.numofitems, item)
