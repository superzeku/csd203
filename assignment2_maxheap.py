import csv
import time

class MaxHeap:
    def __init__(self):
        self.heap = [] 

    def size(self):
        return len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx][0] > self.heap[parent][0]:
            self.swap(idx, parent)
            self.heapify_up(parent)

    def heapify_down(self, idx):
        left = 2*idx + 1
        right = 2*idx + 2
        largest = idx

        if left < self.size() and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < self.size() and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != idx:
            self.swap(idx, largest)
            self.heapify_down(largest)

    def insert(self, book):
        self.heap.append(book)
        self.heapify_up(self.size() - 1)

    def search(self, isbn):
        for item in self.heap:
            if item[0] == isbn:
                return item
        return None  

    def delete_root(self):
        if self.size() == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root

    def delete_isbn(self, isbn):
        for i in range(self.size()):
            if self.heap[i][0] == isbn:
                deleted = self.heap[i]
                self.heap[i] = self.heap[-1]
                self.heap.pop()
                if i < self.size():
                    self.heapify_up(i)
                    self.heapify_down(i)
                return deleted
        return None


def load_books(path):
    books = []
    with open(path,encoding = "utf-8-sig") as f:
        data = csv.DictReader(f)
        for r in data:
            books.append((r["ISBN"], r["Book-Title"], r["Book-Author"], r["Year-Of-Publication"], r["Publisher"]))
    return books


if __name__ == "__main__":
    heap = MaxHeap()
    books = load_books("books.csv")

    print("Total books:", len(books))

    # Insert timing
    t0 = time.perf_counter()
    for b in books:
        heap.insert(b)
    t_insert = time.perf_counter() - t0

    # Search a middle element to avoid bias
    mid_isbn = books[len(books)//2][0]
    t0 = time.perf_counter()
    found = heap.search(mid_isbn)
    t_search = time.perf_counter() - t0

    # delete first/root
    t0 = time.perf_counter()
    heap.delete_root()
    t_del_root = time.perf_counter() - t0

    # delete specific ISBN
    target = "3406475914"
    t0 = time.perf_counter()
    heap.delete_isbn(target)
    t_del_target = time.perf_counter() - t0

    print("Insert time :", t_insert)
    print(f"Search time ({mid_isbn}) :", t_search)
    print("Delete root :", t_del_root)
    print(f"Delete ISBN {target} :", t_del_target)

    if found:
        print("\nFound:", found[0], "-", found[1])
    else:
        print("\nNot found!")

"""
Insertion time was measured, and searching was evaluated by selecting a middle element to avoid bias,
since the heap structure does not guarantee ordering for efficient search. 
Results show that inserting all items primarily costs O(log n) per operation,
while searching is O(n) due to scanning the heap. Deleting the first element (the root) was faster
because the maximum element is always at the root and only requires re-heapifying. 
In contrast, deleting the book with ISBN 3406475914 took longer, since the heap first must linearly 
locate the element before rebalancing. Overall, the Max-Heap performs efficiently for insertions and 
root deletion, but searching and arbitrarily deleting a specific ISBN is slower.
"""