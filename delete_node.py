class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if root.data < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def printInorder(root):
    if root:
        printInorder(root.left)
        print root.data,
        printInorder(root.right)

def findMin(root):
    temp = root
    while(temp):
        if temp.left is None:
            break
        temp = temp.left
    return temp

def findMax(root):
    temp = root
    while(temp):
        if temp.right is None:
            break
        temp = temp.right
    return temp

def deleteNode(root, key):
    if root is None:
        return root
    if root.data < key:
        root.right = deleteNode(root.right, key)
    elif root.data > key:
        root.left = deleteNode(root.left, key)
    else:
         if root.left is None:
             temp = root.right
             root = None
             return temp
         elif root.right is None:
             temp = root.left
             root = None
             return temp
         temp = findMin(root.right)
         root.data = temp.data
         root.right = deleteNode(root.right, temp.data)
    return root



if __name__=='__main__':
    root = None
    root = insert(root,30)
    root = insert(root,40)
    root = insert(root,35)
    root = insert(root,20)
    root = insert(root,60)
    print "Inorder : ",
    printInorder(root)
    root = deleteNode(root, 30)
    print "\nInorder : ",
    printInorder(root)
    min = findMin(root)
    max = findMax(root)
    print "\nMinumum element:%d "%min.data
    print "Maximum element: %d"%max.data
