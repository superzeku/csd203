from arraystructure import *

class ArrQueue(ArrayStructure):
    def __init__(self, cap=10):
        super().__init__(cap)
        self.fidx = 0
        self.length = 0

    def is_full(self):
        return self.length == self.capacity

    def is_empty(self):
        return self.length == 0

    def increase_cap(self):
        new_capacity = self.capacity * 2  # Gấp đôi dung lượng
        new_array = [None] * new_capacity

        # Di chuyển các phần tử cũ sang mảng mới
        for i in range(self.length):
            old_idx = (self.fidx + i) % self.capacity
            new_array[i] = self.arrayNodes[old_idx]
        
        self.arrayNodes = new_array
        self.capacity = new_capacity
        self.fidx = 0  # Đặt lại front index về 0 sau khi mở rộng
        print(f"Capacity increased to {self.capacity}")

    def enqueue(self, x):
        newNode = Node(x)
        if self.is_full():
            self.increase_cap()

        lidx = (self.fidx + self.length) % self.capacity
        self.arrayNodes[lidx] = newNode
        self.length += 1
        print(f"enqueue: x={x}, fidx={self.fidx}, lidx={lidx}, length={self.length}")

    def dequeue(self):
        if self.is_empty():
            return None
        
        temp_node = self.arrayNodes[self.fidx]
        self.arrayNodes[self.fidx] = None
        self.fidx = (self.fidx + 1) % self.capacity
        self.length -= 1
        print(f"dequeue: value={temp_node.data}, fidx={self.fidx}, length={self.length}")
        
        return temp_node.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Queue elements:")
        current_idx = self.fidx
        for _ in range(self.length):
            print(self.arrayNodes[current_idx].data, end=" ")
            current_idx = (current_idx + 1) % self.capacity
        print()

# --- Đoạn code test ---

# Khởi tạo một hàng đợi với dung lượng nhỏ
aqueue = ArrQueue(cap=3)

print("--- Enqueue 3 elements ---")
for i in range(3):
    aqueue.enqueue(i)

print("\n--- Display after enqueue ---")
aqueue.display()

print("\n--- Dequeue 2 elements ---")
aqueue.dequeue()
aqueue.dequeue()

print("\n--- Display after dequeue ---")
aqueue.display()

print("\n--- Enqueue more elements to trigger capacity increase ---")
aqueue.enqueue(3)
aqueue.enqueue(4)
aqueue.enqueue(5)

print("\n--- Final display ---")
aqueue.display()