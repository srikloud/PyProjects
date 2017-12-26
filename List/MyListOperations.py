
def listops():
    l = [0,1,2,3,4,5,6,7,8,9]
    print(l)
    #l.append(5)
    print(l)
    #print(l.pop(0))  # Deletes the element
    print(l)
    print(l.count(1)) # Returns the number of times element repeated
    #print(l.clear())
    #print(l.extend(5))
    print(l[3:])
    print(len(l))
    print(l[len(l):])
    #print(l)
    l.append(10)
    l.extend([12,13,14])
    #l.append([[[15,[16,17]]]])
    l.append([[[[[[[[[[[[[[[15, [16, 17]]]]]]]]]]]]]]]])
    print(l)
    out = []
    l = []
    for i in range(100):
        l = [l, i]

    def flatten(l):
        for i in l:
            #print(i)
            if isinstance(i,(list,tuple)):
                print('hello')
                #print(out)
                #print(i)
                out.extend(flatten(i))
                #print(out)
            else:
                out.append(i)
                #print(out)
                #print(out)
            print(out)


    flatten(l)


listops()

