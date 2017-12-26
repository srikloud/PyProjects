
from linkedlist_pkg.Node import Node

class LinkedList(object):

    def __init__(self):
        print('In Linkedlist')
        self.head = None

    def insertstart(self, data):
        print('In insertstart')
        newnode = Node(data)

        if self.head is None:
            print('In if')
            self.head = newnode

        else:
            print('In else')
            if self.head is not None:
                newnode.nextnode = self.head
                self.head = newnode


    def traverslist(self):
        actualnode = self.head
        listcount = 0;
        while actualnode is not None:
            print('in traverslist')
            listcount = listcount+1
            print('%d' % actualnode.data)
            #print('%d' % 'listcount' + listcount)
            actualnode = actualnode.nextnode
        return listcount


    def removenode(self,loc):
        print('In removenode')
        actualnode = self.head
        listcount = 0;
        while listcount <= loc:
            #print('in traverslist')
            print(listcount)_+8u8u=
            d = actualnode.data
            print(d)
            nex = actualnode.nextnode
            print(nex)
            #print('%d' % 'listcount' + listcount)
            actualnode = actualnode.nextnode
            #print(actualnode)
            if listcount == loc:


            listcount = listcount + 1




