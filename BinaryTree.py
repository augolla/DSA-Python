class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree(object):

    def __init__(self):
        self.root=None
        self.length=0

    def insert(self,data):
        newNode=Node(data)
        if self.root is None:
            self.root=newNode
            self.length+=1
        else:
