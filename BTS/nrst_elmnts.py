def nrst_elmnts_bst(l,ele,right,left):
    print(l)
    print(left)
    print(right)
    print(ele)
    mid = left+right//2
    print("mid"+ str(mid))
    print(l[mid+1])
    print(l[mid-1])


l = [10,20,30,40,50,60,70,80,10]
nrst_elmnts(l,60,len(l)-1,left=0)

