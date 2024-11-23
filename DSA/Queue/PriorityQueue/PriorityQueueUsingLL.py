#Priority Queue using Linked List

class Node:
    def __init__(self, val = None, priority = None, next = None):
        self.val = val 
        self.priority = priority
        self.next = next


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.item_size = 0

    def isEmpty(self):
        return self.head is None
    
    def push(self, val, priority):
        node = Node(val, priority)

        if self.isEmpty() or self.head.priority > priority:
            # insert at the beginning
            node.next = self.head
            self.head = node
        else:
            # insert at the right place in the linked list, based on the priority from low to high
            temp = self.head

            while temp.next is not None and temp.next.priority <= priority:
                # move to the next node
                temp = temp.next

            # now insert the node , suppose we have 1->2->3 and we want to insert 2.5, then we will insert 2.5 between 2 and 3
            node.next = temp.next
            temp.next = node

        self.item_size += 1
    
    def pop(self):
        if self.head is None:
            print("Priority queue is empty")
            return
        else:
            temp=self.head
            self.head = self.head.next
            self.item_size -= 1
        return temp.val

    def peek(self):
        if self.isEmpty():
            print("Priority queue is empty")
            return
        else:
            return self.head.val
        
    def display(self):
        if self.isEmpty():
            print("Priority queue is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.val, end="->")
                temp = temp.next
            print("None")

    def size(self):
        return self.item_size
    
pq = PriorityQueue()
pq.push(10, 3)
pq.push(20, 1)
pq.display()
pq.push(30, 2)
pq.push(40, 2)
pq.display()
print("Popped Element=",pq.pop())
pq.display()
print("Peek Element=",pq.peek())
print("Size of the Priority Queue=",pq.size())
            