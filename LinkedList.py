class Node(object):
    """docstring for ."""

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):
    """docstring for ."""

    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    '''O(1)'''
    def insertHead(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.length+1
        else:
            prevHead=self.head
            self.head=newNode
            self.head.next=prevHead
            self.length+1
    def showList(self):
        currentNode=self.head
        while currentNode.next:
            print(currentNode.data)
            currentNode=currentNode.next

list=LinkedList()
list.insertHead(100)
list.insertHead(200)
list.insertHead(300)
list.showList()
list.insertHead(400)
list.insertHead(500)
list.showList()
