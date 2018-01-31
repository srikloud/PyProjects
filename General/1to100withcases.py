import numpy as np
def oneto100withcases():
    y = ["fuzzbuzz" if (x%3 ==0 and x%5 == 0) else "buzz" if np.mod(x, 5) == 0 else "fuzz" if (x%3 ==0) else x for x in range(1,100)]

    print(y)



oneto100withcases()
