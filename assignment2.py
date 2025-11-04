import time
import csv

class Node:
    def __init__(self,isbn,title,author,year,publisher):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root is None
    def insert(self,isbn,title,author,year,publisher):
        newNode = Node(isbn,title,author,year,publisher)
        if self.is_empty():
            self.root = newNode
            return
        current = self.root
        while True:
            if isbn < current.isbn:
                if current.left is None:
                    current.left = newNode
                    return
                current = current.left
            elif isbn > current.isbn:
                if current.right is None:
                    current.right = newNode
                    return
                current = current.right
            else: return 
    def search(self,isbn):
        current = self.root
        while current is not None:
            if current.isbn == isbn: return current
            if isbn < current.isbn: current = current.left
            else: current = current.right
        return None
    def find_most_right(self,node):
        while node.right:
            node = node.right
        return node
    def delete_bycopy(self,isbn):
        def delete_rec(node,isbn):
            if node is None: return node
            if isbn < node.isbn:
                node.left = delete_rec(node.left,isbn)
            elif isbn > node.isbn:
                node.right = delete_rec(node.right,isbn)
            else:
                if node.left is None: 
                    return node.right
                if node.right is None:
                    return node.left
                
                temp = self.find_most_right(node.left)
                node.isbn = temp.isbn
                node.title = temp.title
                node.author = temp.author
                node.year = temp.year
                node.publisher = temp.publisher

                node.left = delete_rec(node.left,temp.isbn)
            return node
        self.root = delete_rec(self.root,isbn)

def load_csv(filename):
    books = []
    with open(filename,encoding = "utf-8-sig") as f:
        data = csv.DictReader(f)
        for r in data:
            books.append((r["ISBN"], r["Book-Title"], r["Book-Author"], r["Year-Of-Publication"], r["Publisher"]))
    return books

bst = BinarySearchTree()
books = load_csv("books.csv")
t0 = time.time()
for b in books:
    bst.insert(*b)
insert_time = time.time() - t0

# Compare the time to delete the first element and the book with the ISBN of 3406475914.
first_isbn = books[0][0]
t0 = time.time()
bst.delete_bycopy(first_isbn)
delete_first_time = time.time() - t0

_isbn = "3406475914"
t0 = time.time()
bst.delete_bycopy(_isbn)
delete_time = time.time() - t0

print(f"Delete first ({first_isbn}): {delete_first_time:.8f}s")
print(f"Delete ISBN {_isbn}: {delete_time:.8f}s")

"""
After running, I saw delete the first element faster than isbn 3406475914.
Because when deleting in a BST, the time mainly depends on how deep the node is located in the tree.
- first element: near a root -> easy to find and delete
- about isbn 3406475914: in a position in the tree depends on insertion order, 
likely deeper on the tree, need more comparisons to locate 
=> deleting the first element took less time than deleting the book with ISBN 3406475914.
"""

"""
The time to store (insert) all records into the BST increases gradually as the tree grows, 
because each insertion requires comparing ISBN values and traversing the tree. 
Since the BST is not guaranteed to be balanced, the average insertion cost is around O(log n)
but can degrade toward O(n) if the tree becomes skewed.

For searching, the time also depends on the depth of the target node. 
In a reasonably balanced BST, search takes O(log n) on average.
However, in an unbalanced tree, worst-case search becomes O(n).
"""