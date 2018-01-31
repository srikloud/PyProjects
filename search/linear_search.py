def ls():
    l = [10,230,3, 40, 4, 69, 3,39, 58, 55, 93]
    search_ele = 4

    for i in range(0, len(l)):
        if l[i] == search_ele:
            print("Search element "+str(search_ele)+" found at position "+ str(i))
            return


ls()