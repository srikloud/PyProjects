class Node(object):
    def __init__(self,data= None, next_node_pntr=None):
        print('in Node')
        self.data = data
        print(self.data)
        self.next_node_pntr = next_node_pntr
        print(self.next_node_pntr)


class LinkedList(object):
    def __init__(self):
        self.head = None
        print(self.head)
    def add_node(self,data):
        self.head = Node(data,self.head)
        print(self.head)



a = LinkedList()
a.add_node(10)
a.add_node(20)







