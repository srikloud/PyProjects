def bsearch_itr(l,left, right, ele):
    low = l[0]
    hig = l[-1]
    print(low)
    print(hig)
    print(len(l))
    print(l[len(l)//2])
    r = 1
    length = len(l)
    mid = length // 2
    while left <= right:
        mid = (left+right)//2

        if ele > l[mid]:
            print("Search Right")
            left = mid+1
        elif ele == l[mid]:
            print("ele found at pos" + str(mid))
            return str(mid)
        else:
            print("search Left")
            right = mid - 1



class Main():
    l = [10,20,30,40,50,60,70,80]
    left = 0
    right = len(l)-1
    bsearch_itr(l,left,right,50)

if __name__ == '__main__':
        Main()

