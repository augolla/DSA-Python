class Stack(object):
    """docstring forStack."""

    """Initialize an empty array"""
    def __init__(self):
        self.stack=[]

    """Adding to the top---We assume array[0] to be bottom since it came in first"""
    def push(self,data):
        self.stack.append(data)

    """Removing the top---array[-1] is first to get out since it came in last.array[0] is bottom"""
    def pop(self):
        self.stack.remove(self.stack[-1])

    """Cheking the top of stack"""
    def peek(self):
        return self.stack[-1]

    """Size"""
    def size(self):
        return len(self.stack)


stack=Stack()
