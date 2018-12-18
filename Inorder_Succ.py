class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def insert(root, new_node):
    if root is None:
        root = new_node
    else:
        if root.data < new_node.data:
            if root.right is None:
                new_node.parent = root
                root.right = new_node
            else:
                insert(root.right, new_node)
        else:
            if root.left is None:
                new_node.parent = root
                root.left = new_node
            else:
                insert(root.left, new_node)

def findMin(node):
    temp = node
    while(temp):
        if temp.left is None:
            break
        temp = temp.left
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

if __name__=='__main__':
    root = Node(35)
    insert(root, Node(30))
    insert(root, Node(31))
    insert(root, Node(20))
    insert(root, Node(40))
    insert(root, Node(10))
    insert(root, Node(60))
    insert(root, Node(50))
    print "Inorder : ",
    printInorder(root)
    print "\nMinimum element: ",
    min = findMin(root.right)
    print min.data
    succ = inorderSuc(root)
    print "Inorder successor of the node %d is %d: "%(root.data,succ.data)

