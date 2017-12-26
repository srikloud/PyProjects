import time

class bigo_minlist():
    def minlist_bonsqr(self):
        l = [1,476,43,645,23,53,1]
        min = l[0]
        print(time.time())
        for i in range(0, len(l)):
            if l[i] <= min:
                min = l[i]
        print(min)
        print(time.time())



b = bigo_minlist()
b.minlist_bonsqr()
