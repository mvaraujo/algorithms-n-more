# bst.py
# 
# Binary Tree (BST) implementation
#
# author Lajos Onodi Neto


import queue


class Node(object):
    """
    BST node that holds reference to left child, right child
    and also to the value stored within itself.
    """
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class Bst(object):
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, value):
        """
        Recursively insert a new value inside the BST.
        Returns true if successful and false if value already exists.
        """
        if(self.root):
            return self.__insert(self.root, value)
        else:
            self.root = Node(value)
            self.size += 1
            return True
        
    def __insert(self, root, value):
        if(root.value == value):
            return False
        elif value < root.value:
            if(root.leftChild):
                return self.__insert(root.leftChild, value)
            else:
                root.leftChild = Node(value)
                self.size += 1
                return True
        else:
            if(root.rightChild):
                return self.__insert(root.rightChild, value)
            else:
                root.rightChild = Node(value)
                self.size += 1
                return True

    def dfs_inorder(self):
        """
        Prints BST content following inorder walking
        """
        self.__inorder(self.root)

    def __inorder(self, root):
        if(root):
            self.__inorder(root.leftChild)
            print(root.value)
            self.__inorder(root.rightChild)
    
    def dfs_preorder(self):
        """
        Prints BST content following preorder walking
        """
        self.__preorder(self.root)

    def __preorder(self, root):
        if(root):
            print(root.value)
            self.__inorder(root.leftChild)
            self.__inorder(root.rightChild)

    def dfs_postorder(self):
        """
        Prints BST content following preorder walking
        """
        self.__postorder(self.root)

    def __postorder(self, root):
        if(root):
            self.__inorder(root.leftChild)
            self.__inorder(root.rightChild)
            print(root.value)
    
    def bfs(self):
         """
         Visits BST nodes following the Breadth-first 
         tree traversal approach
         """
         node_queue = [self.root]
         node_bfs_order = []
         self.__bsf(node_queue, node_bfs_order)
         return node_bfs_order

    def __bsf(self, node_queue, node_bfs_order):
        if node_queue:
            cur_node = node_queue.pop()
            if cur_node.leftChild:
                node_queue.insert(0, cur_node.leftChild)
            if cur_node.rightChild:
                node_queue.insert(0, cur_node.rightChild)
            node_bfs_order.append(cur_node.value)
            self.__bsf(node_queue, node_bfs_order)
    
    def search_value(self, value):
        """
        Search for a given value inside the BST.
        """
        return self.__search_value(self.root, value)

    def __search_value(self, root, value):
        if(root.value == value):
            return True
        if(value < root.value):
            if(root.leftChild):
                return self.__search_value(root.leftChild, value)
            else:
                 return False
        else:
            if(root.rightChild):
                return self.__search_value(root.rightChild, value)
            else:
                return False

if __name__ == '__main__' :
    bst = Bst()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(6)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(20)
    bst.insert(12)
    bst.insert(14)
    bst.insert(13)
    bst.insert(21)
    bst.insert(22)
    bst.insert(23)
    bst.insert(24)
    bst.insert(25)
    bst.bfs()