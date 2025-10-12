from binarysearchtree import *

class AVLTree(BinarySearchTree):
    def left_rotate(self, node):
        new_root = node.right
        new_left = new_root.left
        new_root.left = node
        node.right = new_left
        return new_root

    def right_rotate(self, node):
        new_root = node.left
        new_right = new_root.right
        new_root.right = node
        node.left = new_right
        return new_root
    def balance_factor(self, node):
        if node == None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, x, node):
        if node == None:
            return Node(x)
        if x < node.data:
            node.left = self.insert(x, node.left)
        elif x > node.data:
            node.right = self.insert(x, node.right)
        else:
            return node 
        return self.balance(node)

    def balance(self, node):
        bf = self.balance_factor(node)
        # Mất cân bằng bên phải
        if bf < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)
        # Mất cân bằng bên trái
        elif bf > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.left_rotate(node.left)
            node = self.right_rotate(node)
        return node

    def avl_insert(self, x):
        self.root = self.insert(x, self.root)

    def find_most_right(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete_bycopy(self, node, x):
        def delete_avl_node(x, node):
            if node is None:
                return node
            if x < node.data:
                node.left = delete_avl_node(x, node.left)
            elif x > node.data:
                node.right = delete_avl_node(x, node.right)
            else:
                # Tìm thấy node cần xóa
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    # Copy giá trị node lớn nhất bên trái
                    most_right_node = self.find_most_right(node.left)
                    node.data = most_right_node.data
                    node.left = delete_avl_node(most_right_node.data, node.left)
            return self.balance(node)
        self.root = self.balance(delete_avl_node(x, node))


if __name__ == "__main__":
    avltree = AVLTree()
    avltree.avl_insert(100)
    avltree.avl_insert(50)
    avltree.avl_insert(120)
    avltree.avl_insert(150)
    avltree.avl_insert(180)
    avltree.avl_insert(200)
    avltree.pre_order()
    avltree.delete_bycopy(avltree.root, 100)
    avltree.pre_order()
