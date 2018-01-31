def max_sum():
    #l = [10,20,30,-10,-50,40, -50, -1, -3]
    l = [-1,-2,-3,-4,-5]
    i = 0
    n = 0
    while i <= len(l)-1:
        print(l[i])
        if l[i] >= 0:
            n = n+l[i]
            i = i+1
        elif l[i] < 0:
            if i != len(l)-1:
                if l[i] > l[i+1]:
                    n = n+l[i]
                    i = i+2
                    print("i > i+1"+str(n))
                elif l[i] < l[i+1]:
                    n = n+l[i+1]
                    i = i+2
                    print("i < i+1" + str(n))
            elif i == len(l)-1:
                i = i+1


    print(n)



max_sum()
