class newnode():
    def __init__(self,value):
        print("inside newnode for " + str(value))
        self.head = value
        self.left = None
        self.right = None

class bt():
    def __init__(self):
        print("inside __init__")
        self.head = None
        self.left = None
        self.right = None
        self.root = None


    def addnode(self,value):
        print("addnode "+str(value))
        if not self.root:
            print("addnode self.root is None")
            self.root = newnode(value)
            print(self.root.head)
            print("self.root " + str(self.root))
        else:
            print("addsubnode self.root is Not None")
            self.addsubnode(value,self.root)

    def addsubnode(self,value,curnode):
        print("addsubnode call for value and curnode "+ str(value)+" "+str(curnode))
        if curnode:
            print("Curnode is not none " + str(curnode))
            if not curnode.left:
                print("curnode befor node creation " + str(curnode))
                print("Curnode.left is none " + str(curnode.left))
                curnode.left = newnode(value)
                curnode = curnode.left
                print("curnode after node creation "+ str(curnode))
            elif curnode.left:
                print("Curnode.left is not none " + str(curnode.left))
                if  value < curnode.left.head:
                    print("curnode.left.head "+ str(curnode.left.head))
                    print("value" + str(value))
                    print("Curnode is not none and < curnode.head " + str(curnode.left))
                    print("*************addsubnode recursive call")
                    self.addsubnode(value,curnode.left)

        else:
            print("curnode is None")



    def printnodes(self):
        if self.root:
            print(self.root)
            print(self.left)
            print(self.right)

b = bt()
b.addnode(50)
b.addnode(40)
b.addnode(35)

b.printnodes()

