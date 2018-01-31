import string

def kth_most_frqnt():
    l = [1,2,3,4,2,3,4,3,2,1,1,2,3,3,2]
    print(l)
    nmbrs = string.digits
    print(len(nmbrs))
    d = {}

    for i in range(0,len(nmbrs)):
        d[i] = 0
    print(d)
    d1 = {}
    for i in range(0,len(l)):
        if l[i] in d:
            d[l[i]] = d[l[i]]+1
    print(d)
    max = 0
    k1 = 0
    v1 = 0
    for k,v in d.items():
        if v > max:
            k1 = k
            v1 = v
            max = v
    print(str(k1)+":"+str(v1))






kth_most_frqnt()
