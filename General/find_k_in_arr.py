import numpy as np
def oddnumber(l,r):

    if l < r:
        for i in range(l,r):
            if np.mod(i,2) != 0:
                print(''.join(i))



oddnumber(1,10)