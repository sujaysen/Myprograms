class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, key):
    if root is None:
        return 0
    if root.data == key:
        return 1
    if root.data < key:
        return search(root.right, key)
    else:
        return search(root.left, key)

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def printInorder(root):
    if root:
        printInorder(root.left)
        print root.data,
        printInorder(root.right)

r = Node(50)
insert(r, Node(30))
insert(r, Node(10))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))
print "BST :",
printInorder(r)
print "\nSearch: ",
if search(r, 10):
    print "Exsist"
else:
    print "Not Exsist"
