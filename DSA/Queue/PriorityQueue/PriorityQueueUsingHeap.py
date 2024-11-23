import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def is_empty(self):
        return len(self.pq) == 0

    def push(self, value, priority):
        heapq.heappush(self.pq, (priority, value))

    def pop(self):
        if self.is_empty():
            print("Priority queue is empty")
            return None
        return heapq.heappop(self.pq)

    def peek(self):
        if self.is_empty():
            print("Priority queue is empty")
            return None
        return self.pq[0]

    def display(self):
        if self.is_empty():
            print("Priority queue is empty")
        else:
            print(self.pq)

    def size(self):
        return len(self.pq)

pq = PriorityQueue()
pq.push(10, 3)
pq.push(20, 1)
pq.display()
pq.push(30, 2)
pq.push(40, 2)
pq.display()
print("Popped:", pq.pop())
pq.display()
print("Peek:", pq.peek())
print("Size:", pq.size())
