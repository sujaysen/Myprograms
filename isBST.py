import myFunction
INT_MAX = 4294967296
INT_MIN = -4294967296

def isBST(node): 
    return (isBSTUtil(node, INT_MIN, INT_MAX)) 
  
def isBSTUtil(node, mini, maxi): 
      
    if node is None: 
        return True
  
    if node.data < mini or node.data > maxi: 
        return False
  
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi)) 

if __name__=='__main__':
    root = None
    root = myFunction.insert(root,4)
    root = myFunction.insert(root,2)
    root = myFunction.insert(root,5)
    root = myFunction.insert(root,1)
    root = myFunction.insert(root,3)

    if isBST(root):
        print "Yes it is BST"
    else:
        print "It is not BST"
