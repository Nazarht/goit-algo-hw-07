

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        
        return node
    
    def find_max(self):
        if self.root is None:
            return None
        
        current = self.root
        while current.right is not None:
            current = current.right
        
        return current.value
    
    def find_min(self):
        if self.root is None:
            return None
        
        current = self.root
        while current.left is not None:
            current = current.left
        
        return current.value
    
    def sum_all(self):
        return self._sum_all(self.root)
    
    def _sum_all(self, node):
        if node is None:
            return 0
        
        return node.value + self._sum_all(node.left) + self._sum_all(node.right)
    
    def display(self):
        self._display(self.root, 0)
    
    def _display(self, node, level):
        if node is not None:
            self._display(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self._display(node.left, level + 1)
