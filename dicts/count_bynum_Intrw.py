from collections import OrderedDict
# Interview
def countbynum():
    n = "10 10 10 50 50 50 50 50 90 90 90 90 90 90 5 5 5 5 20 20 30 30 30"
    l = n.split()
    d = OrderedDict()
    x = 0
    for i in range(0, len(l)):
        if l[i] in d:
            d[l[i]]=d[l[i]]+1
        else:
            d[l[i]]=1
    print(d)

    ll = []
    for k,v in d.items():
        ll.append(str(int(v)))
        ll.append(str(int(k)))
    print(ll)
    str1 = ' '.join(ll)
    print(str1)





countbynum()
