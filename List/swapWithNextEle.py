def swapNextElement_List(l):
    print(l)
    for i in range(0,len(l)-1,2):
        print(i)
        l[i],l[i+1]=l[i+1],l[i]
        print(l)

swapNextElement_List([1,2,3,4,5,6,7])


