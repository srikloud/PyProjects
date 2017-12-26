# noinspection PyCallingNonCallable
def printlistindex():
    l = [11, 22, 33, 44, 55, 56, 37, 28, 69]
    out = []
    '''for i in range(0,len(l)):
        out.append(l[i])
        print(i)
        print(out[i])'''
    print(len(l))
    print(l[-len(l)])
    print(l.sort())
    print(l)


    l.append('Srikanth')
    print(l)

    # Convert ListofString to a String
    out = []
    listofStrings = ['My','Name','Is','Srikanth']
    ''.join(listofStrings)
    print(out)
    #print(los.split(sep=','))

    # Convert list of Integers to a single Integer.

    listofNumbers = [1,2,3]
    lon = str(listofNumbers)
    #lon = ''.join(str(n) for n in listofNumbers)
    #lon = ''.join(listofNumbers)
    print(lon[:])

    #Convert a list to tuple()
    t = tuple(l)
    print('list to tuple'+ str(t))

    # Convert a list to set()
    s = set(l)
    print(s)

    a_list = [1, 2, 3, 44]
    print(a_list)
    b_list = a_list
    print(b_list)
    b_list.append(4)
    print(b_list)
    print(a_list)
    c_list = a_list[:]
    print(c_list)
    c_list.append(5)
    print(c_list)
    print(b_list)
    print(a_list)

    #Convert list to Dict
'''
    for i in l:
        zip(i,l[i])
    print(out)
    print(isinstance(out[:], dict))
        #print(dict(zip(i,l[i])))
'''


a_list = [1, 2, 3,44]
print(a_list)
b_list = a_list
print(b_list)
#    ''' b_list.append(4)
#     print(a_list)
'''c_list = a_list[:]
print(c_list)
c_list.append(5)
print(c_list)
print(a_list)'''




printlistindex()
