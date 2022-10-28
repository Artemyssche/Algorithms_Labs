import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.height = 1

class AvlTree:
    def getHeight(self, root):
        if not root:
            return 0
        else:
            return root.height

    def insert_node(self, root, key):

        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def getBalance(self, root):
        if not root:
            return 0
        else:
            return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

myTree = AvlTree()
root = None
root = myTree.insert_node(root, 10)
root = myTree.insert_node(root, 20)
root = myTree.insert_node(root, 30)
root = myTree.insert_node(root, 40)
root = myTree.insert_node(root, 50)
root = myTree.insert_node(root, 25)

print(myTree.getHeight(root))

myTree.preOrder(root)