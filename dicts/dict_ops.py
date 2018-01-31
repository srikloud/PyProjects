def dict_ops():
    d1 = {'Name':'kick','Age':'6','Class':'1st'}
    print(d1['Name'])
    print(d1['Age'])
    print(d1['Class'])
    d1['School'] ='Olivera'
    print(d1)
    d1['School']

    for k,v in d1.items():
        print(k+":"+v)

    d2 = {}
    print(d2)

    d2 = {n:n**2 for n in range(1,10)}  -- Dictionary Comprehension
    print(d2)

dict_ops()