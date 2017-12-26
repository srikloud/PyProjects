class new_node():
    def __init__(self,value=None,nextnode=None):
        self.value = value
        self.nextnode = nextnode

class ll_sorted():
    def __init__(self):
        self.root = None

    def addnode(self,value):
        print("#########addnode  "+str(value))
        if not self.root:
            self.root = new_node(value)
            print(self.root.value)
            print(self.root.nextnode)
        else:
            if self.root.value < value:
                print("self.root.value < value")
                self.root = new_node(value, self.root)
            elif self.root.value > value:
                print("Inside While")
                self.swap_nodes(self.root,value)

    def swap_nodes(self,readnode,value, prevnode=None):
        print("*****Enter into Swapnodes*******8")
        print("readnode.value"+str(readnode.value))
        print("readnode.nextnode" + str(readnode.nextnode))
        print("value" + str(value))
        if readnode.value > value:
            print("if readnode.value > value:")
            prevnode = readnode
            if readnode.nextnode != None:
                readnode = readnode.nextnode
                print(readnode)
                self.swap_nodes(readnode, value, prevnode)
            else:
                print("create node as lastnode with nextnode none")
                newnode = new_node(value, None)
                print("update the previous lastnode with nextnode")
                readnode.nextnode = newnode

        else:
            print("else  readnode.value < value")
            print("prevnode " + str(prevnode))
            print("self.root" + str(self.root))
            print("prevnode.value " + str(prevnode.value))
            print(readnode.value)
            print(value)
            if readnode.nextnode == None:
                print("If no more nextnodes to process means new value need to inserted right before Last element")
                self.add_intermediate_node(value, readnode, prevnode)
            else:
                print("if new value is right in between existing(not last or not root) nodes then insert and update the previous element")
                newnode = new_node(value,readnode)
                prevnode.nextnode = newnode


    def add_intermediate_node(self,value,nextnode,prevnode):
        newnode = new_node(value,nextnode)
        if prevnode == self.root:
            print("prevnode == self.root")
            print("self.root.nextnode" + str(self.root.nextnode))
            self.root.nextnode = newnode
            print("self.root.nextnode" + str(self.root.nextnode))
        else:
            prevnode.nextnode = newnode

    def print_node(self):
        print("In Print_Node")
        print("self.root" + str(self.root))
        print("self.root.value" + str(self.root.value))
        while self.root.value:
            print(self.root.value)
            self.root = self.root.nextnode


l = ll_sorted()
l.addnode(10)
l.addnode(30)
l.addnode(15)
l.addnode(8)
l.addnode(12)
l.addnode(45)
l.addnode(5)
l.addnode(22)


l.print_node()

