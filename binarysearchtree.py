class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root == None
    def insert(self,x):
        if self.is_empty(): 
            self.root = Node(x)
            return
        newNode = Node(x)
        current = self.root
        while True:
            if x > current.data:
                if current.right == None:
                    current.right = Node(x)
                    return
                current = current.right
            elif x < current.data:
                if current.left == None:
                    current.left = Node(x)
                    return
                current = current.left
            else:
                print("exist")
                return
    def insert_recursion(self,x):
        if self.is_empty():
            self.root = Node(x)
            return
        current = self.root
        def insert_rec(current):
            if current == None: return Node(x)
            if x > current.data:
                current.right = insert_rec(current.right)
            elif x < current.data:
                current.left = insert_rec(current.left)
            return current
        insert_rec(current)
    def find_most_right(self, node):
        if node.right == None: return node
        return self.find_most_right(node.right)
    def delete_bycopy(self,x):
        def delete_node(x,node):
            if node == None: return node
            if x < node.data: node.left = delete_node(x,node.left)
            elif x > node.data: node.right = delete_node(x,node.right)
            else:
                if node.left == None: 
                    node = node.right
                    return node
                elif node.right == None:
                    node = node.left
                    return node
                most_right_node = self.find_most_right(node.left)
                node.data = most_right_node.data
                node.left = delete_node(most_right_node.data,node.left)
            return node
        self.root = delete_node(x,self.root)
    def delete_bymerge(self,x):
        def delete_node(x,node):
            if node == None: return node
            if x < node.data: node.left = delete_node(x,node.left)
            elif x > node.data: node.right = delete_node(x,node.right)
            else:
                if node.left == None:
                    node = node.right
                    return node
                elif node.right == None:
                    node = node.left
                    return node
                most_right_node = self.find_most_right(node.left)
                most_right_node.right = node.right
                node = node.left
            return node
        self.root = delete_node(x,self.root)
    def height(self,node):
        if node == None: return 0
        return max(self.height(node.left),self.height(node.right)) + 1
    def height_tree(self):
        return self.height(self.root)
    def search(self,x):
        def search_node(x,node):
            if node == None or node.data == x: return node
            if x < node.data: return search_node(x,node.left)
            return search_node(x,node.right)
        return search_node(x,self.root)
    def pre_order(self):
        def preorder_node(node):
            if node == None: return
            print(node.data,end = " ")
            preorder_node(node.left)
            preorder_node(node.right)
        if self.is_empty(): print("Empty")
        preorder_node(self.root)
        print()
    def post_order(self):
        def postorder_node(node):
            if node == None: return
            postorder_node(node.left)
            postorder_node(node.right)
            print(node.data,end = " ")
        if self.is_empty(): print("Empty")
        postorder_node(self.root)
        print()
    def in_order(self):
        def inorder_node(node):
            if node == None: return
            inorder_node(node.left)
            print(node.data,end = " ")
            inorder_node(node.right)
        inorder_node(self.root)
        print()

if __name__ == "__main__":
    bstree = BinarySearchTree()
    bstree.insert_recursion(50)
    bstree.insert_recursion(100)
    bstree.insert_recursion(30)
    bstree.insert_recursion(150)
    bstree.insert_recursion(90)
    bstree.insert_recursion(200)

    print(bstree.height_tree())
    bstree.pre_order()
    bstree.delete_bycopy(100)
    bstree.pre_order()
    bstree.delete_bymerge(50)
    bstree.pre_order()