from arraystructure import *
class ArrQueue(ArrayStructure):
    def __init__(self,cap = 10):
        super().__init__(cap)
        self.fidx = 0
    def increaseCap(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.length):
            new_array[i] = self.arrayNodes[(self.fidx + i) % self.capacity]
        self.arrayNodes = new_array
        self.capacity = new_capacity
        self.fidx = 0 
    def enqueue(self,x):
        if self.isEmpty():
            self.fidx=0
            self.arrayNodes[self.fidx] = Node(x)
            self.length += 1
            return
        if self.isfull():
            self.increaseCap()
        lidx = (self.fidx + self.length) % self.capacity
        self.arrayNodes[lidx] = Node(x)
        self.length+=1
    def dequeue(self):
        if self.isEmpty():
            return None
        tmp = self.arrayNodes[self.fidx]
        self.arrayNodes[self.fidx] = None
        self.fidx = (self.fidx+1)%self.capacity
        self.length-=1
        return tmp
    def front(self):
        if self.isEmpty():
            return None
        return self.arrayNodes[self.fidx]
    def display(self):
        if self.isEmpty():
            print("Empty")
            return
        current = self.fidx
        for _ in range(self.length):
            print(self.arrayNodes[current].data,end=" ")
            current = (current + 1)%self.capacity
        print()
aqueue = ArrQueue(5)
print(aqueue.arrayNodes)
for i in range(10):aqueue.enqueue(i)
aqueue.dequeue()
aqueue.dequeue()
aqueue.dequeue()
for i in range(5): aqueue.enqueue(2*i)
aqueue.dequeue()
print("Full Array:", [n.data if n else None for n in aqueue.arrayNodes])
print(aqueue.front().data)
#aqueue.display()
