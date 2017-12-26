def deepList():
    a = []
    for i in range(100):
        a = [a, i]
    print(a)

deepList()