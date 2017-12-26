class node():
    def __init__(self,value=None,nextnode=None):
        print("node__init()___")
        self.value = value
        print("self.value"+str(self.value))
        self.nextnode = nextnode
        print("self.nextnode"+str(self.nextnode))

class ll():
    def __init__(self):
        print("ll__init()___")
        self.root = None

    def addnode(self,value):
        if self.root == None:
            self.root = node(value)
            print("self.root"+str(self.root))
        else:
            print("self.root not none")
            self.root = node(value, self.root)
            print("self.root" + str(self.root))

    def printnodes(self):
        readnode = self.root
        while readnode:
            print(readnode.value)
            readnode = readnode.nextnode


    def joinnodes(self,l1,l2):
        readnode = l1.root
        while readnode:
            if readnode.nextnode == None:
                readnode2 = l2.root
                while readnode2:
                    self.addnode(readnode2.value)
                    readnode2 = readnode2.nextnode
            readnode = readnode.nextnode
        self.printnodes()


    def convert_nodes_to_list(self,ll):
        print("@@@@@@@@@@@@@@@@@@@@2convert_nodes_to_list")
        readnode = ll.root
        list1 = list()
        while readnode:
            list1.append(readnode.value)
            readnode = readnode.nextnode
        print(list1)
        list_set = set(list1)
        print(list_set)











l = ll()
l.addnode(10)
l.addnode(20)
l.addnode(40)
l.addnode(60)
l.addnode(30)
l.addnode(15)


l2 = ll()
l2.addnode(100)
l2.addnode(200)
l2.addnode(40)
l2.addnode(600)
l2.addnode(30)
l2.addnode(150)

#l.printnodes()
#l2.printnodes()

#l3 = ll()
l.joinnodes(l,l2)
#l.printnodes()
l.convert_nodes_to_list(l)

