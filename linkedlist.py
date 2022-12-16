##implementation of a linked list
class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
if __name__ == '__main__':##keep track of running scripts

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(123)
    second = Node(278)
    third = Node("helooooooo\n")
    fourth=Node(890)        
    # Connect nodes
    linked_list.head.next = second
    second.next = third
    third.next= fourth

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next