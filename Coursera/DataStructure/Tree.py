class Node(object):
    def __init__ (self, value):
        self.value= value
        self.left= None
        self.right=  None

class BTestTree(object) :
    def __init__ (self, root):
        self.root = Node(root)

    def Treeprint (self,tv_type):
        if tv_type=="Preorder" :
            return self.printpreorderTraversal(Tree.root,"")
        elif tv_type == "Inorder" :
            return self.printinorderTraversal(Tree.root,"")
        elif tv_type == "Postorder" :
                return self.printpostorderTraversal(Tree.root,"")
        else :
            print ("Invalid ...")


    #preorder root =>Left=>Right
    def printpreorderTraversal(self,start, traversal):
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.printpreorderTraversal(start.left,traversal)
            traversal = self.printpreorderTraversal(start.right,traversal)
        return traversal
    #inorder Left=>root=>Right
    def printinorderTraversal(self,start, traversal):
        if start:
            traversal = self.printinorderTraversal(start.left,traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.printinorderTraversal(start.right,traversal)
        return traversal

        #inorder Left=>Right=> root
    def printpostorderTraversal(self,start, traversal):
        if start:
                traversal = self.printpostorderTraversal(start.left,traversal)
                traversal = self.printpostorderTraversal(start.right,traversal)
                traversal += (str(start.value) + " - ")
        return traversal



Tree =   BTestTree(1)
Tree.root.left= Node(2)
Tree.root.right= Node(3)
Tree.root.left.left= Node(4)
Tree.root.left.right= Node(5)
Tree.root.right.left= Node(6)
Tree.root.right.right= Node(7)
print(Tree.Treeprint("Postorder"))
