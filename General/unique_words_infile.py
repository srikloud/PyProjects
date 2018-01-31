def unique_words():
    f1 = "I am good good"
    f2 = "You are good"
    f3 = f1.split()
    print(f3)
    f4 = f2.split()
    print(f4)

    d ={}
    i = 1
    for i in range(0,len(f3)):
        if f3[i] in d:
            d[f3[i]] = d[f3[i]]+1
        else:
            d[f3[i]] = 1
    print(d)

    for i in range(0,len(f4)):
        if f4[i] in d:
            d[f4[i]] = d[f4[i]]+1
        else:
            d[f4[i]] = 1
    print(d)
    print(d.items())
    print(d.keys())
    print(d.values())

    #for i in range(0,len(d.keys())):
        #print()

    print("unique workds in a file")
    for k,v in d.items():
        if v==1:
            print(str(k)+":"+str(v))





unique_words()