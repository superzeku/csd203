from arraystructure import *
class MinHeap(ArrayStructure):
    def insert(self, x):
        if self.isfull(): self.increaseCap()
        else: 
            self.arrayNodes[self.length] = Node(x)
            self.heapify_up(self.length)
            self.length+=1
    def pre_order(self):
        def preorder(idx):
            if idx >= self.length or self.arrayNodes[idx] == None: return
            print(self.arrayNodes[idx].data, end=" ")
            preorder(2*idx+1)
            preorder(2*idx+2)
        preorder(0)
        print()
    def in_order(self):
        def inorder(idx):
            if idx >= self.length or self.arrayNodes[idx] == None: return
            inorder(2*idx+1)
            print(self.arrayNodes[idx].data, end=" ")
            inorder(2*idx+2)
        inorder(0)
        print()
    def heapify_up(self, idx):
        if idx == 0: return
        parent = (idx-1)//2
        if self.arrayNodes[parent].data > self.arrayNodes[idx].data:
            self.arrayNodes[parent], self.arrayNodes[idx] = self.arrayNodes[idx], self.arrayNodes[parent]
            self.heapify_up(parent)
    def heapify_down(self, idx):
        left = 2*idx+1
        right = 2*idx+2
        smallest = idx
        if left < self.length and self.arrayNodes[left].data < self.arrayNodes[smallest].data: smallest = left
        if right < self.length and self.arrayNodes[right].data < self.arrayNodes[smallest].data: smallest = right
        if smallest != idx:
            self.arrayNodes[smallest], self.arrayNodes[idx] = self.arrayNodes[idx], self.arrayNodes[smallest]
            self.heapify_down(smallest)
    def search(self, x):
        def search_node(x, idx):
            if idx >= self.length or self.arrayNodes[idx] == None: return -1
            if self.arrayNodes[idx].data == x: return idx
            if self.arrayNodes[idx].data > x: return -1
            left = search_node(x, 2*idx+1)
            if left != -1: return left
            return search_node(x, 2*idx+2)
        return search_node(x, 0)
    def delete(self, x):
        idx = self.search(x)
        if idx == -1: return
        self.arrayNodes[idx] = self.arrayNodes[self.length-1]
        self.length -= 1

        parent = (idx-1)//2
        if idx > 0 and self.arrayNodes[parent].data > self.arrayNodes[idx].data:
            self.heapify_up(idx)
        else:    
            self.heapify_down(idx)

if __name__ == "__main__":
    minheap = MinHeap()
    minheap.insert(3)
    minheap.insert(15)
    minheap.insert(9)
    minheap.insert(17)
    minheap.insert(20)
    minheap.insert(11)
    minheap.insert(14)
    minheap.insert(22)
    minheap.insert(23)
    minheap.insert(25)
    minheap.insert(27)
    minheap.insert(18)
    minheap.insert(12)
    minheap.pre_order()
    minheap.delete(20)
    minheap.pre_order()