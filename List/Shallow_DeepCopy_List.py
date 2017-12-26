import sys
from copy import deepcopy
def listcopy():
    l1 = [1,2,3,4,5]
    l2 = l1
    print(l1)
    print(l2)
    l2.append(6)
    print(l1)
    print(l2)
    l3 = l2
    print(l3)
    l3.append(7)
    print(l1)
    print(l2)
    print(l3)
    l4 = l3[:]
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    l4.append(8)
    print(l1)
    print(l2)
    print(l3)
    print(l4)

    l5 = [10,20,30,[40,50],[60,70]]
    l6 = l5
    print(l5)
    print(l6)
    l6.append(80)
    print(l5)
    print(l6)
    l7 = l6[:]
    print(l5)
    print(l6)
    print(l7)
    l7.append(90)
    print(l5)
    print(l6)
    print(l7)
    l7[6] = 81
    print(l5)
    print(l6)
    print(l7)
    l7[3][1] = 31
    print(l5)
    print(l6)
    print(l7)
    l8 = deepcopy(l6)
    print(l8)
    l8[3][1] = 32
    print(l5)
    print(l6)
    print(l7)
    print(l8)














listcopy()