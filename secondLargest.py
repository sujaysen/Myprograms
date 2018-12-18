import delete_node

if __name__=='__main__':
    root = None
    root = delete_node.insert(root, 34)
    root = delete_node.insert(root, 30)
    root = delete_node.insert(root, 50)
    root = delete_node.insert(root, 10)
    root = delete_node.insert(root, 20)
    root = delete_node.insert(root, 80)
    root = delete_node.insert(root, 90)
    root = delete_node.insert(root, 45)
    print "Inorder :",
    delete_node.printInorder(root)
    max = delete_node.findMax(root)
    root = delete_node.deleteNode(root, max.data)
    max = delete_node.findMax(root)
    print "\nSecond largest element is: %d"%max.data
    

