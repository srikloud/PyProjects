class fifo_node():
    def __init__(self,data = None, nextnode = None):
        self.data = data
        self.next = nextnode


class ll_fifo():
    def __init__(self):
        self.root = None
        self.tail = None

    def insert(self,data):
        node = fifo_node(data)
        if not self.root:
            self.root = node

        if self.tail:
            self.tail.next = node
        self.tail = node






    def print_nodes(self):
        print("*************Print NODES*************")
        if self.root !=None:
            print("self.root is not none")
            readnode = self.root
            print(readnode)
            while readnode != None:
                print("readnode.nextnode is not none")
                print(readnode)
                print(readnode.data)
                readnode = readnode.next

    def print_nodes_asc(self,ll_new):
        ll_asc = list()
        for i in range(0,len(ll_new)):
            i = (-1*(i+1))
            ll_asc.append(ll_new[i])
        print("In Asc Order")
        print(ll_asc)

    def print_nodes_desc(self):
        head = self.root
        l = None
        tl = None
        l2 = 0
        ll = list()
        ll_new = list()
        while head:
            ll.append(head.data)
            head = head.next
        #print(ll)
        for j in range(0,len(ll)):
            for i in range(0,len(ll)):
                if ll[i] not in ll_new:
                    if l == None:
                        l = ll[i]
                    if ll[i] >= l:
                        l = ll[i]
            l2 = l
            ll_new.append(l2)
            #print(l2)
            l = None
        print("In Desc Order")
        print(ll_new)
        self.print_nodes_asc(ll_new)









l = ll_fifo()
l.insert(10)
l.insert(20)
l.insert(0)
l.insert(30)
l.insert(40)
l.insert(50)
l.insert(-1)
l.insert(60)

l.print_nodes()
l.print_nodes_desc()


