# Priority queue is a data structure that stores elements in a queue and allows the insertion of elements based on their priority.

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return len(self.pq) == 0 or self.pq == []
    
    # insert element in the priority queue based on the priority from low to high, low will have higher priority
    def push(self, val, priority):
        #we will using tuple to store the element and its priority
        idx=0

        while idx < len(self.pq) and self.pq[idx][1] <= priority: # if the priority of the element is less than the priority of the element at idx then we will break the loop, else we will increment the idx, here we check the priority from low to high
            idx+=1

        self.pq.insert(idx, (val, priority))

    def pop(self):
        if self.isEmpty():
            print("Priority queue is empty")
            return
        else:
            self.pq.pop(0) # pop the element with highest priority

    def peek(self):
        if self.isEmpty():
            print("Priority queue is empty")
            return
        else:
            return self.pq[0]
    
    def display(self):
        if self.isEmpty():
            print("Priority queue is empty")
            return
        else:
            print(self.pq)

    def size(self):
        return len(self.pq)
    

pq=PriorityQueue()
pq.push(10, 3)
pq.push(20, 1)
pq.display()
pq.push(30, 2)
pq.push(40, 2)
pq.display()
pq.pop()
pq.display()
print(pq.peek())
print(pq.size())

#Output:
# [(30, 2), (40, 2), (10, 3)]