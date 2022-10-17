class Node:
    def __init__(self , data , left=None , right=None):
        self.data = data
        self.left = left
        self.right = right
        
class BST:
    
    height_of_tree = -1

    def __init__(self , node):
        self.root = node
#----------------------------------------------------------------
    def __contains__(self , data):
        return self.contains_helper(self.root,data)
    
    def contains_helper(self,root,data):
        if root == None:
            return False
        elif root.data == data:
            return True
        elif data < root.data:
            return self.contains_helper(root.left, data)
        elif data > root.data:
            return self.contains_helper(root.right, data)
        
#----------------------------------------------------------------
    def insert(self ,value):
        self.help_insert(self.root,value)

    def help_insert(self,start,value):
        if value == start.data:
            return

        if value < start.data:
            if start.left:

                self.help_insert(start.left,value)
            else:
                start.left = Node(value)
        else:       
            if start.right:
                self.help_insert(start.right,value)
            else:
                start.right = Node(value)
#----------------------------------------------------------------     
    def inorder(self):
        return self.help_inorder(self.root)
    
    def help_inorder(self,abc):
        store = []
        if abc:
            store += self.help_inorder(abc.left)
            store.append(abc.data)
            store += self.help_inorder(abc.right)
            
        return store
#----------------------------------------------------------------
    def preorder(self):
        return self.help_preorder(self.root)
    
    def help_preorder(self,abc):
        store = []
        if abc:
            store.append(abc.data)
            store += self.help_preorder(abc.left)
            store += self.help_preorder(abc.right)
        return store

#----------------------------------------------------------------

    def postorder(self):
        return self.help_postorder(self.root)
    
    def help_postorder(self,abc):
        store = []
        if abc:
            store += self.help_postorder(abc.left)
            store += self.help_postorder(abc.right)
            store.append(abc.data)
        return store
#----------------------------------------------------------------

    def level_order(self):
        store =[]
        queue =[]
        queue.append(self.root)
        #stack.append(self.root.data)
        while queue:
            abc =len(queue)
            
            self.height_of_tree += 1
            
            for i in range(abc):
                elem = queue.pop(0)
                store.append(elem.data)
                if elem.left:
                    #stack.append(elem.left.data)
                    queue.append(elem.left)
                if elem.right:
                    #stack.append(elem.right.data)
                    queue.append(elem.right)
        return store
#----------------------------------------------------------------
    
    def diameter(self):
        root_start =self.root
        longest=[0]
        
        def search(root):
           # print("in search")
            if root is None:
                return -1
            left = search(root.left)
            right = search(root.right)
            longest[0] = max(longest[0],2+left+right)
            
            return 1+max(left,right)
        
        search(root_start)
        return longest[0]        
#----------------------------------------------------------------
        
    def delete(self,key):
        curr = self.root
        if key ==  self.root.data:
            if not self.root.right and not self.root.left:
                 self.root = None
            elif not curr.right and curr.left:
                pre = self.find_predessor(curr)
                pre.right =curr.right
                pre.left = curr.left
                self.root =pre
            else:
                #print("in elif root")
                succ = self.find_successor(curr)  
                succ.left = curr.left
                succ.right = curr.right
                self.root = succ
        else:        
            while curr:
                #print("in while of delete")
                if key < curr.data:
                    prev=curr
                    curr = curr.left
                elif key > curr.data:
                    prev = curr
                    curr =curr.right
                elif curr.data == key:
                    break

            if not curr.left and not curr.right:
                if curr.data > prev.data:
                    prev.right = None
                else: 
                    prev.left  = None
            elif curr.left and not curr.right:
                prev.left = curr.left
            elif curr.right and not curr.left:
                prev.right = curr.right
            else:
                    succ = self.find_successor(curr)  
                    succ.left = curr.left
                    succ.right = curr.right

                    if succ.data < prev.data:
                        prev.left = succ
                        print(prev.data)
                    else:
                        prev.right =succ

                
#----------------------------------------------------------------      
    def find_predessor(self,root):
        prev = root
        root = root.left
        if root.right:
            while root.right:
                prev = root
                root = root.right
            if root.left:
                prev.right = root.left
            else:
                prev.right = None
        else:
            prev.left =root.left
            
        return root
    
#----------------------------------------------------------------
            
    def find_successor(self,root):
        prev = root
        root = root.right
        if root.left:
            while root.left:
                prev = root
                root = root.left

            if root.right:
                prev.left = root.right
            else:
                prev.left = None
        else:
            prev.right = root.right
        return root
    
#----------------------------------------------------------------

    def height(self):
        
        self.level_order()
        return self.height_of_tree
    
        
#---------------------------------------------------------------- 

    def max(self):
        abc = self.preorder()
        return max(abc)
                        
        
if __name__ == '__main__':
    
    nodel = Node(5, Node(1), Node(7))
    noder = Node(15, Node(12), Node(17))
    
    tree = BST (Node (10,nodel,noder))
        
    print("----output starts----")
    print()
    print("----Maximum----")
    maxi = tree.max()
    print("maximum element is:",maxi)
    #----------------------------------------------------------------
    print()
    print("----Contains----")
    abc = 15 in tree
    abc1 =16 in tree
    print("contains is ",abc)
    print("contains is",abc1)
    #----------------------------------------------------------------
    print()
    print("----Height----")
    height = tree.height()
    print("Height of tree is:",height)
    #----------------------------------------------------------------
    print()
    print("----Diameter----")
    diameter = tree.diameter()
    print("Diameter is:", diameter)
    #----------------------------------------------------------------
    print()
    print("---Inorder----")
    inorder = tree.inorder()
    print("Inorder is :",inorder)
    #----------------------------------------------------------------
    
    print()
    print("---Preorder----")
    inorder = tree.preorder()
    print("Preorder is :",inorder)
    #----------------------------------------------------------------
    
    print()
    print("---Postorder----")
    inorder = tree.postorder()
    print("Postorder is :",inorder)
    #----------------------------------------------------------------
    
    print()
    print("---Level Order----")
    inorder = tree.level_order()
    print("Level order is :",inorder)
    #----------------------------------------------------------------
    
    t2 = BST (Node (10, None, Node(15)))

    print()
    print("----Output tree 2----")
    print("---Insert---")
    t2.insert(12)
    t2.insert(16)
    t2.insert(9)
    t2.insert(11)
    #----------------------------------------------------------------
    print()
    print("---Level Order---")
    level= t2.level_order()
    print("Level order is:", level)
    #----------------------------------------------------------------
        
    print()
    print("---Inorder---")
    inorder = t2.inorder()
    print("Inorder is:", inorder)
    
    #----------------------------------------------------------------
        
    print()
    print("---preorder---")
    inorder = t2.preorder()
    print("preorder is:", inorder)
    #----------------------------------------------------------------
        
    print()
    print("---Postorder---")
    inorder = t2.postorder()
    print("postorder is:", inorder)
    
    #----------------------------------------------------------------
        
    print()
    print("---Diameter---")
    inorder = t2.diameter()
    print("Diamater is:", inorder)
    #----------------------------------------------------------------
    print()
    print("---Delete---")
    t2.delete(10)
    
    
    #----------------------------------------------------------------
        
    print()
    print("---Inorder after deletion---")
    inorder = t2.inorder()
    print("Inorder after deletion:", inorder)
    #----------------------------------------------------------------
    
    print()
    print("-------Third tree output starts ---------")
    t3 = BST(Node(10,None,None))
    print()
    print("---Inorder is---")
    inorder= t3.inorder()
    print(inorder)
    #----------------------------------------------------------------
    print()
    print("---Diameter---")
    abc=t3.diameter()
    print("Diameter is:",abc)
    #----------------------------------------------------------------
    print()
    print("---Height---")
    height = t3.height()
    print("Height is: ", height)
    
    print()
    print("---Delete---")
    t3.delete(10)
    abc= t3.inorder()
    print(abc)
    
    
    
