def kth_largest(l,k):
    for i in range(0,k):
        #print(i)
        if i<k-1:
            l.pop(max(l) - 1)
        else:
            print(max(l))

kth_largest([1,2,3,4,5,6,7],2)