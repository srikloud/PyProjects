class node():
    def __init__(self,value=None, nextnode=None):
        self.value = value
        self.nextnode = nextnode

class llist():
    def __init__(self):
        self.root = None

    def addnode(self,value):
        self.root = node(value,self.root)

    def printnodes(self):
        readnode = self.root
        while readnode:
            print(readnode.value)
            readnode = readnode.nextnode

    def swapnodes(self):
        tempnode = self.root
        traversenode = self.root
        print("traversenode"+str(traversenode))
        print("traversenode.value" + str(traversenode.value))
        print("traversenode.nextnode" + str(traversenode.nextnode))
        while traversenode:
            print(traversenode.nextnode)
            if traversenode.nextnode == None:
                print("traversenode not none")
                print(tempnode.value)
                print(traversenode.value)
                self.root.value = traversenode.value
                print(self.root.value)
                print(tempnode.value)
                traversenode.value = tempnode.value
                print(traversenode.value)
                traversenode = None
            else:
                print("in else")
                print(traversenode.nextnode)
                traversenode = traversenode.nextnode
        print("Hello"+ str(self.root.value))





l = llist()
l.addnode(10)
l.addnode(20)
l.addnode(30)
l.addnode(40)
l.printnodes()
l.swapnodes()
l.printnodes()

