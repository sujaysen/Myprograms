import numpy as np
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printInorder(root):
    if root:
        printInorder(root.left)
        print root.data,
        printInorder(root.right)

def printPreorder(root):
    if root:
        print root.data,
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print root.data,

def printthatlevel(root, i):
    if root is None:
        return
    if i == 1:
        print root.data,
    elif i > 1:
        printthatlevel(root.left, i-1)
        printthatlevel(root.right, i-1)


def printLevelorder(root):
    h = height(root)
    for i in range(1, h+1):
        printthatlevel(root, i)


def height(root):
    if root is not None:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
    else:
        return 0

def size(root):
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1

def findMax(root):
    if root is None:
        return -np.inf
    res = root.data
    lmax = findMax(root.left)
    rmax = findMax(root.right)
    if res < lmax:
        res = lmax
    if res < rmax:
        res = rmax
    return res

def findMin(root):
    if root is None:
        return np.inf
    res = root.data
    lmin = findMin(root.left)
    rmin = findMin(root.right)
    if res > lmin:
        res = lmin
    if res > rmin:
        res = rmin
    return res

def insert(root, node):
    if root is None:
        root = node
        return
    if root.left is None:
        insert(root.left,node)
    else:
        insert(root.right, node)



root = Node(100)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(500)
root.right.left = Node(6)
root.right.right = Node(1)
insert(root, Node(666))
print "Preorder-DFS: ",
printPreorder(root)
print "\nInorder-DFS: ",
printInorder(root)
print "\nPostorder-DFS: ",
printPostorder(root)
print "\nLevelorder-BFS: ",
printLevelorder(root)
print "\nSize:",
print size(root)
print "Height:",
print height(root)
print "Maximum:",
print findMax(root)
print "Minimum:",
print findMin(root)

