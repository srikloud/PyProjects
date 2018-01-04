def bsearch_rec(l,left,right,ele):

    if left <= right:
        mid = (left+right)//2
        if ele == l[mid]:
            print("ele found at pos" + str(mid))
            return str(mid)
        elif ele > l[mid]:
            print("search right")
            print("recursive call initiated")
            bsearch_rec(l,mid+1,right,ele)
        elif ele < l[mid]:
            print("search left")
            print("recursive call initiated")
            bsearch_rec(l, left, mid -1, ele)
    else:
        print(str(ele)+" element not found")

class Main():
    l = [10,20,30,40,50,60,70,80,90,100]
    ele = 55
    print(l)
    print("Trying to find "+str(ele))
    length = len(l)
    left = 0
    right = length-1

    found = bsearch_rec(l,left,right,ele)
    #print("ele found at pos" + str(found))


if __name__ == "__main__":
    Main()
