def mergelists(a,b):
    c=[]
    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    print(a)
    print(b)
    print(c+a+b)


#mergelists([1,2,3,10,15],[5,20,30,40,50])

def mergeUnsortedLists(a,b):
    a=a+b
    for j in range(0,len(a)-1):
        print(j)
        for i in range(0, len(a)-j):
            print(i)
            #print("i "+str(a[i]))
            if i+1<len(a)-j:
                if a[i] > a[i+1]:
                    a[i],a[i+1] = a[i+1],a[i]
                    print(a)






mergeUnsortedLists([10,23,1,5,3,7,6],[5,20,30,40,50])
