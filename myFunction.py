class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def maxx(a,b):
    if a >= b:
        return a
    else:
        return b
    
def insert(root, key):
    if root is None:
        return Node(key)
    if root.data < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def maxDepth(node): 
    if node is None: 
        return 0 ;  
  
    else : 
  
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
  
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
  
def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right)) + 1
            
def search(root, key):
    if root is None:
        return 0
    if root.data == key:
        return 1
    if root.data < key:
        return search(root.right, key)
    else:
        return search(root.left, key)

def findMin(node):
    temp = node
    while(temp):
        if temp.left is None:
            break
        temp = temp.left
    return temp

def findMax(node):
    temp = node
    while(temp):
        if temp.right is None:
            break
        temp = temp.right
    return temp

def inorderSuc(node):
    if node.right is not None:
        return findMin(node.right)
    p = node.parent
    while(p):
        if node != p.right:
            break
        node = p
        p = p.parent
    return p


def printInorder(root):
    if root:
        printInorder(root.left)
        print root.data,
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print root.data,

def printPreorder(root):
    if root:
        print root.data,
        printPreorder(root.left)
        printPreorder(root.right)


