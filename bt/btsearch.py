class node():
    def __init__(self, data = None, left = None, right = None):
        self.value = data
        self.left = left
        self.right = right


class binarytree():
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.root = None

    def addnode(self,data):
        if self.root == None:
            self.root = node(data)
            print(self.root)
            print(self.root.value)
            print(self.root.left)
            print(self.root.right)

        if self.root != None:
            self.addsubnode(data, self.root)

    def addsubnode(self,data,curnode):
        if data:
            if data < curnode.value:
                if not curnode.left:
                    print("********1***********")
                    curnode.left = node(data)
                    newnode = curnode.left
                    print(newnode)
                    print(newnode.value)
                    print(newnode.left)
                    print(newnode.right)
                else:
                    print("********2****************************")
                    print("call recursive addsubnode")
                    self.addsubnode(data, curnode.left)
            elif data > curnode.value:
                if not curnode.right:
                    print("********3**********8")
                    curnode.right = node(data)
                    newnode = curnode.right
                    print(newnode)
                    print(newnode.value)
                    print(newnode.left)
                    print(newnode.right)
                else:
                    print("********4************************")
                    print("call recursive addsubnode")
                    self.addsubnode(data, curnode.right)

    def printnodes(self):
        print("***********Print NODES**********")
        curnode = self.root
        print(curnode)
        print("########################3In Order Traversal")
        if self.root:
            print("call root.left")
            self.printsubnodes_in(self.root.left)
            #print("call root.value")
            print(self.root.value)
            #print("call root.right")
            self.printsubnodes_in(self.root.right)
        else:
            print("empty binary tree")

        print("#######################Pre Order Traversal")
        if self.root:
            print("call root.left")
            self.printsubnodes_pre(self.root.left)
            #print("call root.value")
            print(self.root.value)
            #print("call root.right")
            self.printsubnodes_pre(self.root.right)
        else:
            print("empty binary tree")


    def printsubnodes_in(self,curnode):
        print("printsubnode IN")
        head = curnode.value
        left = curnode.left
        right = curnode.right
        if curnode.left:
            #print("printsubnode left")
            self.printsubnodes_in(curnode.left)
        print("printsubnode head")
        print(head)
        if curnode.right:
            print("printsubnode right")
            self.printsubnodes_in(curnode.right)


    def printsubnodes_pre(self,curnode):
        print("printsubnode IN")
        head = curnode.value
        left = curnode.left
        right = curnode.right
        print(head)
        if curnode.left:
            #print("printsubnode left")
            self.printsubnodes_pre(curnode.left)
        print("printsubnode head")
        if curnode.right:
            print("printsubnode right")
            self.printsubnodes_pre(curnode.right)










b = binarytree()
b.addnode(70)
b.addnode(45)
b.addnode(25)
b.addnode(35)
b.addnode(40)
b.addnode(42)
b.addnode(30)
b.addnode(80)
b.addnode(85)
b.printnodes()