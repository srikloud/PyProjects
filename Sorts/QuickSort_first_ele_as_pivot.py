#source: http://en.literateprograms.org/Quicksort_(Python)
def qsort_lcomplist():
    """Quicksort using list comprehensions"""
    print("list")
    print(list)
    if list == []:
        return []
    else:
        pivot = list[0]
        print("pivot")
        print(pivot)
        print("lesser")
        lesser = qsort1([x for x in list[1:] if x < pivot])
        print("lesserdata")
        print(lesser)
        print("greater")
        greater = qsort1([x for x in list[1:] if x >= pivot])
        print("greater data")
        print(greater)
        print("final result")
        return lesser + [pivot] + greater

numbers1 = [100,6,3,32,85,23,1,9,336,23,123]
numbers=[2,3,6,2,10,20,40,1]


#print qsort1(numbers)

def qsort(l,first,last):
    print(l)
    if first < last:
        #print(l)
        sp=qsort_partition(l,first,last)
        print("left sort")
        qsort(l,first,sp-1)
        print("right sort")
        qsort(l,sp+1,last)
        print(l)

def qsort_partition(l,first,last):
    pi=l[first]
    print(pi)
    #lo=1
    lo=first+1
    print(lo)
    #print(len(l))
    #print()
    #hi=len(l)-1
    hi=last
    print(hi)

    done=False

    while not done:

        while lo<=hi and pi>=l[lo]:
            lo=lo+1
            print("low")
            print(lo)
            #print("low value")
            #print(l[lo])

        while lo<=hi and pi<=l[hi]:
            hi=hi-1
            print("high")
            print(hi)
            #print(l[hi])

        if hi<lo:
            done=True
            #print("done")
            #print(done)
            #print(l)
            #print(lo)
            #print(l[lo])
            #print(hi)
            #print(l[hi])
        else:
            #print("else")
            #print(str(l[lo])+' '+str(l[hi]))
            l[lo],l[hi]=l[hi],l[lo]
            print("after swap")
            print(str(l[lo]) + ' ' + str(l[hi]))
            print(l)

    print("swap pivot")
    l[first],l[hi]=l[hi],l[first]
    print(l)
    print("hi after swap pivot")
    print(hi)
    return hi




#qsort(numbers,0,len(numbers)-1)

#qsort_partition(numbers)



def qs(list,first,last):
    if first<last:
        print(list)
        split=qs_partition(list,first,last)
        print("split")
        print(list[split])
        qs(list,first,split-1)
        qs(list,split+1,last)
        print(list)


def qs_partition(list,first,last):
    pi=list[first]
    print("pi")
    print(pi)
    left=first+1
    right=last
    done=False
    print(list)
    while not done:
        print("while1")
        while left<=right and list[left]<=pi:
            print("while2")
            left=left+1
            print("left")
            print(left)

        while left<=right and list[right]>=pi:
            print("while3")
            right=right-1
            print("right")
            print(right)

        if right<=left:
            done=True
            print(done)
        else:
            list[left],list[right]=list[right],list[left]
            print("else")
            print(list)

    list[first],list[right]=list[right],list[first]
    print("After pi swap")
    print(list)
    return right

print("hellp")
#qsort(numbers,0,len(numbers)-1)
#qs(numbers,0,len(numbers)-1)



def qs1(list,first,last):
    if first < last:
        print("hellpo")
        qs_split = par(list,first,last)
        qs1(list,first,qs_split-1)
        qs1(list,qs_split+1,last)


def par(list,first,last):
    print("par")

    pivot=list[first]
    print("pivot")
    print(pivot)

    left=first+1
    right=last
    done=False
    while not done:
        #print(done)

        while left<=right and list[left] <= pivot:
            left=left+1
            print(left)

        while left<=right and list[right] >= pivot:
            right=right-1
            print(right)

        print(list)
        if right<=left:
            done=True
            print(done)
        else:
            print("else")
            list[left],list[right]=list[right],list[left]
            print("list")
            print(list)
    #if done==True:
    list[first],list[right]=list[right],list[first]
    print(list)
    return right


qs1(numbers,0,len(numbers)-1)



















