class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def insertAtBegining(self, x):

        # code here
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        return new_node.data




    # function appends data x at the end of list and returns new head
    def insertAtEnd(self, x):
        new_node = Node(x)
        if self.head is None:
            new_node = self.head
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node






if __name__ == '__main__':
        ll = Linked()
        ll.insertAtBegining(10)
        ll.insertAtEnd(20)
        ll.printList()



