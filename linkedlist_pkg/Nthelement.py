class node():
    def __init__(self,head = None, tail = None):
        self.head = head
        self.tail = tail

class ll():
    def __init__(self):
        self.root = None
        self.counter = 0
    def add(self,data):
        if not self.root:
            self.root = node(data)
        else:
            self.addnode(data,self.root)

    def addnode(self,data,nextnode):
        self.root = node(data,nextnode)


    def printnodes(self):

        if self.root:
            print(self.root.head)
            self.counter +=1
            if self.root.tail:
                self.printsubnodes(self.root.tail)

    def printsubnodes(self,nextnode):
        if nextnode:
            self.counter +=1
            print(nextnode.head)
            nextnode = nextnode.tail
            self.printsubnodes(nextnode)
        print(self.counter)

    #def nth_node(self):

l = ll()
l.add(10)
l.add(20)
l.add(30)
l.add(45)
l.add(60)
l.printnodes()