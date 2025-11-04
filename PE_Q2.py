class Model:
    def __init__(self,n,m,y):
        self.year = y
        self.month = m
        self.name = n
    def cmp(self, other):
        m = (self.year, self.month, self.name)
        o = (other.year, other.month, other.name)
        if m > o : return 1
        if m < o: return -1
        return 0
    def __str__(self):
        return f"{self.name} - {self.month} - {self.year}"
    
class BSTNode:
    def __init__(self,x):
        self.model = x
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root == None
    def insert(self,x):
        newNode = BSTNode(x)
        if self.is_empty(): 
            self.root = newNode
            return
        current = self.root
        while True:
            if x.cmp(current.model) > 0:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            elif x.cmp(current.model) < 0:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            else:
                print("exist")
                return
    def search_by_name(self, name):
        def search(node):
            if node is None:
                return None
            if node.model.name == name:
                return node.model
            left = search(node.left)
            if left: return left
            return search(node.right)
        return search(self.root)
    def in_order(self):
        def inorder_node(node):
            if node == None: return
            inorder_node(node.left)
            print(node.model)
            inorder_node(node.right)
        inorder_node(self.root)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(Model("FlAN", 9, 2021))
    bst.insert(Model("BERT", 10, 2018))
    bst.insert(Model("Trans", 6, 2017))
    bst.insert(Model("Chatgpt", 11, 2022))
    bst.insert(Model("GPT-3", 5, 2020))
    bst.insert(Model("DeepSeek", 1, 2024))
    bst.in_order()
    print(bst.search_by_name(Model("DeepSeek", 1, 2024)))