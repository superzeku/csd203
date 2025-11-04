"""
1. Mass-Ordered Data Structure: If you wish to organize this data in a structure that is ordered by 
mass, which data structure would be most appropriate? Discuss the advantages and potential 
drawbacks of using this data structure (access, insert, delete, search…) [2 points] 

==> To save and sort by mass, I want to use AVL Tree to organize and optimize this data.
* Advantages:
- Automatically maintain mass order
- access, insert, delete, search with time complexity O(logn) (with balanced tree)
* Disadvantages:
- Need time to balanced the tree 
- Hard and complex to implement

2. Equatorial Diameter Processing: Suppose the functionality of the application needs to process 
these objects one by one, in order of their equatorial diameter. List all the data structures that you 
have learned in this course, could be used for this purpose. Identify the most efficient data structure. 
[2 points] 

==> To meet this requirement, I can use several data structures I have learnt: Linked list, Array, 
Priority queue and Binary search tree.
* The most efficient is Priority queue (max heap/ min heap) because it is fast in term of insert/delete data.

3. Programming Task: You have to implement one of the data structures, including (1) singly 
linked list, (2) doubly linked list, (3) circularly linked list, (4) array-based stack, (5) linked-list
based stack, (6) array-based queue, (7) linked-list-based queue, (8) array-based priority queue, (9) 
linked-list-based priority queue according to your Student ID number.Your data structure is equal 
to the result of two last numbers in your Student ID number % 9 + 1. [6 points]

* My Student ID is DE201068 ==> Number = (68%9+1) = 6 ==> I will implement array-based queue
-> I will use circular array to define an array-based queue data structure
"""

class ArrayQueue:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.arrqueue = [None]*capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def increase_size(self):
        new_capacity = self.capacity * 2
        new_arrqueue = [None]*new_capacity
        for i in range(self.size):
            new_arrqueue[i] = self.arrqueue[(self.front+i)%self.capacity]
        self.arrqueue = new_arrqueue
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size - 1

    def enqueue(self,value):
        if self.is_full(): 
            self.increase_size()
        self.rear = (self.rear+1) % self.capacity
        self.arrqueue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        value = self.arrqueue[self.front]
        self.front = (self.front+1) % self.capacity
        self.size -= 1
        return value
    
    def front_value(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        return self.arrqueue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        i = self.front
        for _ in range(self.size):
            print(self.arrqueue[i], end = " ")
            i = (i+1)%self.capacity
        print()

queue = ArrayQueue(3)
queue.enqueue("Mercury")
queue.enqueue("Venus")
queue.enqueue("Earth")
queue.display()
print(queue.size)
queue.enqueue("Mars")  
queue.display()
print(queue.size)
print(queue.dequeue())
queue.display()


