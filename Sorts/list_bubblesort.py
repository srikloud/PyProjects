class bblsort():
    def bsort(self,l):
        for i in range(1, len(l)):
            for j in range(0, len(l)-1-i):
                print(str(l[j]) +' '+ str(l[j+1]))
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    print("After Sort")
                    print(str(l[j]) + ' ' + str(l[j+1]))
        print(l)

b = bblsort()
l = [10,3,4,65,23,64,32,33]
b.bsort(l)
