class Queue(object):
    """docstring for Queue."""

    """Initialize an empty array"""
    def __init__(self):
        self.queue=[]

    """Adding to the bottom---We assume array[0] to be first or top since it came in first"""
    def addToQueue(self,data):
        self.queue.append(data)

    """Removing the top(array[0])"""
    def pop(self):
        self.queue.remove(self.queue[0])

    """Cheking the top of queue"""
    def peek(self):
        return self.queue[0]

    """Size"""
    def size(self):
        return len(self.queue)


queue=Queue()
