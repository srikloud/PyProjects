class Node():
    def __init__(self, data = None, next_node_pntr=None):
        print("in Node init")
        self.data = data
        print('1')
        print(self.data)
        self.next_node_pntr = next_node_pntr
        print('2')
        print(self.next_node_pntr)

    def set_data(self,data):
        self.data=data
        print('3')
        print(self.data)

    def get_data(self):
        return self.x

    def get_next_node(self):
        return self.y


    def set_next_node_pntr(self,next_node_pntr=None):
        self.next_node_pntr=next_node_pntr
        print('4')
        print(self.next_node_pntr)

class Linkedlist():
    def __init__(self,head=None):
        print("init LL")
        self.head = head
        print(self.head)


class app(object):
    def __init__(self,head=None):
        print("init app")
        self.head = head
        print(self.head)

    def insert(self, data):
        nextnode = Node()
        nextnode.set_data(data)
        nextnode.set_next_node_pntr(self.head)
        self.head=nextnode
        print('5')
        print(self.head)

    def remove_node(self, data):
        current_head = self.head
        current_data = current_head.data
        print(6)
        while current_head.data != data:
            print(7)
            print(current_data)
            prev = current_head
            current_head = current_head.next_node_pntr
            print(current_head)
            current_data = current_head.data
            print(8)
            print(current_data)
        print(prev)
        print(current_head)
        print(current_head.next_node_pntr)

        prev.next_node_pntr = current_head.next_node_pntr
        print(prev.next_node_pntr )

    def print_nodes(self):
        print('In Print Nodes')
        current_head = self.head
        print(current_head.data)
        next_ptr = current_head.next_node_pntr
        while next_ptr != None:
            #print(9)
            print(next_ptr.data)
            #print(next_ptr)
            next_ptr = next_ptr.next_node_pntr
            #print(next_ptr.data)
            #print(next_ptr)

    def find_node_by_index(self,index):
        print("In find_node_by_index")
        print(110)
        counter = 0
        current_head = self.head
        prev_pntr = None
        data = current_head.data
        next_pntr = current_head.next_node_pntr
        #print(next_pntr.data)
        while counter != index:
            #print(111)
            #print(counter)
            prev_pntr = current_head
            next_pntr = current_head.next_node_pntr
            data = next_pntr.data
            current_head = next_pntr
            counter += 1
        #print(prev_pntr,next_pntr,data,counter)
        return prev_pntr,next_pntr,data,counter

    def delete_by_index(self,index):
        p, n, d, c = a.find_node_by_index(index)
        print(p,n,d,c)
        new_node = n.next_node_pntr
        #print(new_node)
        #print(new_node.data)
        p.next_node_pntr = new_node
        a.print_nodes()





#ll = Linkedlist()
a = app()
a.insert(data=10)
a.insert(data=20)
a.insert(data=30)
a.insert(data=40)
a.insert(data=50)
#a.remove_node(data=20)
a.print_nodes()
#p,n,d,c = a.find_node_by_index(2)
a.delete_by_index(2)





