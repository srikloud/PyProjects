def rem_dup_from_list(l):
    print(set(l))

    d={}
    x=[]
    for i in range(0, len(l)-1):
        if l[i] in d.keys():
            d[l[i]] = d[l[i]]+1
            #x.append(l[i])
            #l.pop(l[i])
        else:
            d[l[i]]=1
    print(d.values()
          )
    print(x)







rem_dup_from_list([1, 1 , 2, 2,3, 3,4, 4,5, 6, 7])