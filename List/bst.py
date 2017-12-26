class node():
    def __init__(self,data):
        self.data = data
        print(self.data)
        self.leftnode = None
        print(self.leftnode)
        self.rightnode = None
        print(self.rightnode)


class bst_operations():

    def __init__(self):
        print("in bst_operations constructor")
        self.root = None

    def insert(self, data):
        print("bst_insert")
        if self.root == None:
            self.root=node(data)
        else:
            print("call _insert")
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        print("***inside call _insert")
        if data < cur_node.data:
            print("******data < curnode.data")
            if cur_node.leftnode == None:
                print("*********leftnode is None")
                cur_node.leftnode = node(data)
            else:
                print("************recursive leftnode call")
                self._insert(data,cur_node.leftnode)
        elif data > cur_node.data:
            print("******data > curnode.data")
            if cur_node.rightnode == None:
                print("*********rightnode is None")
                cur_node.rightnode = node(data)
            else:
                print("************recursive rightnode call")
                self._insert(data,cur_node.rightnode)


    def print_bst(self):
        print("*********************Print the Node elements")
        curnode = self.root
        if curnode == None:
            print('Tree is empty')
        else:
            self._print_bst(curnode)

    def _print_bst(self,printnode):

            curnode = printnode
            if curnode != None:
                self._print_bst(curnode.leftnode)
                print(curnode.data)
                self._print_bst(curnode.rightnode)




b = bst_operations()
b.insert(50)
b.insert(5)
b.insert(75)
b.insert(3)
b.insert(10)
b.insert(9)
b.insert(2)
b.insert(1)
b.insert(30)
b.insert(55)
b.print_bst()


