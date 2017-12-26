class node():
    def __init__(self,data):
        print('node__init')
        print(self)
        self.value = data
        print('value'+str(self.value))
        self.leftvalue = None
        print(self.leftvalue)
        self.rightvalue = None
        print(self.rightvalue)



class bst():
    def __init__(self):
        print('bst__init')
        print(self)
        self.curnode = None

    def insert(self,data):
        print('insert' + str(data))
        print(self)
        if self.curnode == None:
            print('curnode is none')
            print(self.curnode)
            self.curnode = node(data)
            print(self.curnode)
        else:
            print('else curnode is not none')
            print(self)
            print(self.curnode)
            print(self.curnode.value)
            print(self.curnode.leftvalue)
            print(self.curnode.rightvalue)
            self.subinsert(self.curnode,data)

    def subinsert(self,curnode,data):
        print('****_insert')
        print(self)
        print(curnode)
        if curnode != None:
            print('******_insert newnode not none')
            print(curnode.value)
            if data < curnode.value:
                print('******_insert newnode not none and data < newnode.value')
                if curnode.leftvalue == None:
                    print('******_insert newnode not none and data < newnode.value and newnode.leftvalue = none')
                    curnode.leftvalue = node(data)
                    print(curnode.leftvalue)
                    print('***************self.curnode.lefvalue updated')

                else:
                    print(curnode.leftvalue.value)
                    print(curnode.leftvalue.leftvalue)
                    print(curnode.leftvalue.rightvalue)
                    print(curnode.leftvalue)
                    print('******_insert newnode not none and data < newnode.value and newnode.leftvalue not none')
                    self.subinsert(curnode.leftvalue,data)
            else:
                print('*******RIGHT Data > node value')
                if curnode.rightvalue == None:
                    curnode.rightvalue = node(data)
                else:
                    self.subinsert(curnode.rightvalue,data)
                    print('***************self.curnode.rightvalue updated')


    def printnodes(self):
        print('*****print nodes*********')
        '''print(self)
        print(self.curnode)
        print(self.curnode.value)
        print(self.curnode.leftvalue)
        print(self.curnode.rightvalue)'''
        if self.curnode == None:
            print('Empty Binary Tree')
        else:
            print('Binary Tree is not empty')
            self.printsubnode(self.curnode)


    def printsubnode(self,rootnode):
        if rootnode != None:
            print('rootnode.leftvalue != None')
            self.printsubnode(rootnode.leftvalue)
            print(rootnode.value)
            self.printsubnode(rootnode.rightvalue)




def main():
    bst = bst()
    bst.insert(70)
    bst.insert(30)
    bst.insert(20)
    bst.insert(10)
    bst.insert(85)
    bst.insert(100)
    bst.printnodes()

if __name__=="__main__":
    main()



'''
bst = bst()
bst.insert(70)
bst.insert(30)
bst.insert(20)
bst.insert(10)
bst.insert(85)
bst.insert(100)
bst.printnodes()
'''