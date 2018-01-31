def bs_recursive(l, lft, rt, ele):
    print("list " + str(l))
    print("left " + str(lft))
    print("right " + str(rt))
    mid = (lft + rt)//2
    print("mid " + str(mid))

    if ele == l[mid]:
        print("element found at position " + str(mid))
        return
    elif ele > l[mid]:
        print("Search right")
        lft = mid + 1
        bs_recursive(l, lft, rt, ele)
    elif ele < l[mid]:
        print("search left")
        rt = mid - 1
        bs_recursive(l, lft, rt, ele)
    else:
        print("element not found")


l = [10,29,30, 40, 50, 50, 70, 90,100]
ele = 10
lft = 0
rt = len(l)-1
bs_recursive(l,lft, rt,ele)
