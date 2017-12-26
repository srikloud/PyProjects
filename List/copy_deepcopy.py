import copy
l1 = [1,2,3,4,5,6]
l2 = l1
print(l1)
print(id(l1))
print(l2)
print(id(l2))

l3 = copy.copy(l1)
print(id(l3))
l3.append(11)
print(l3)

l4 = copy.deepcopy(l1)
print(id(l4))
l4.append(113)
print(l4)

l5 = copy.deepcopy(l3)
print(l5)
l5.append(12)
print(l5)
print(l3)

l6 = [1,2,3,[4,5],6]
l7 = l6
l7.append(8)
l6[2]=10
l8 = copy.deepcopy(l6)
print(l6)
print(l8)
l8[2] = 20
print(l8)
l8[3][1] = 30
print(l6)
print(l8)


