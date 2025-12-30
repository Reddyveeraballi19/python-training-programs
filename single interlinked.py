class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def iterate(head):
    temp = head
    while temp!=None:
        print(temp.val, end=" ")
        temp = temp.next


head = Node(5)
head.next = Node(10)
head.next.next = Node(4)

iterate(head)
