l = [2,5,3,1,12,9,4,7,10]
ll = 0
l2 = 0
l3 = list()
la = 0
lo = 0
for j in range(0,len(l)):
    for i in range(0,len(l)):
        if l[i] not in l3:
            if l[i] > la:
                la = l[i]
    lo = la
    l3.append(lo)
    la = 0
    print(l3)