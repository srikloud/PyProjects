def bs_iter(l,lft,rt,ele):
    while lft <=rt:
        print("print left " + str(lft))
        print("print right " + str(rt))
        print("Search element " + str(ele))
        mid = (lft + rt) // 2
        print("middle position " + str(mid))

        if l[mid] == ele:
            print("element found at position "+ str(mid))
            return
        elif ele > l[mid]:
            print("search right")
            lft = mid+1
        elif ele < l[mid]:
            print("search left")
            rt = mid-1
        else:
            print("element not found")

l=[20,30,40,50,55,60,70,80,90,100]
ele = 50
lft = 0
rt = len(l)
bs_iter(l,lft,rt,ele)