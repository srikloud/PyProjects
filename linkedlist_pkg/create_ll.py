class node():
    def __init__(self,data=None,nextnode=None):
        print("node__init__ for data  "+str(data))
        self.data = data
        self.nextnode = nextnode


class ll():
    def __init__(self):
        print("ll__init")
        self.root = None
        self.nextnode = None


    def create_node(self,data):
        self.nextnode=self.root
        self.root = node(data,self.nextnode)
        print(self.root)
        print(self.root.data)
        print(self.root.nextnode)

    def print_ll_nodes(self):
        print("*****print_all_nodes*****")
        readnode = self.root
        while readnode != None:
            print(readnode)
            print(readnode.data)
            readnode = readnode.nextnode

    def print_nodes_desc(self):
        l = list()
        print("*****print_nodes_desc")
        readnode = self.root
        while readnode != None:
            l.append(readnode.data)
            readnode = readnode.nextnode
        #print(l)
        l1 = l
        print(l)
        self.ll_sort_desc(l)

    def ll_sort_desc(self,l):
        print("************ll_sort")
        ll = 0
        l2 = 0
        la = 0
        l3 = list()
        for j in range(0, (len(set(l)))):
            for i in range(0, len(set(l))):
                if l[i] not in l3:
                    if l[i] >= la:
                        la = l[i]
            lo = la
            if lo not in l3:
                l3.append(lo)
            la = 0
        print(l3)
        self.ll_sort_asc(l3)

    def ll_sort_asc(self,l):
        l_asc = list()
        for i in range(0,len(l)):
            i = (i+1)*(-1)
            l_asc.append(l[i])
        print(l_asc)


l = ll()
l.create_node(70)
l.create_node(20)
l.create_node(30)
l.create_node(20)
l.create_node(70)
l.create_node(0)
l.create_node(10)

l.print_ll_nodes()
l.print_nodes_desc()



