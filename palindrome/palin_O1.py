def pd(l):
    print(l)
    l2 = []
    for i in range(len(l)//2):
        print(l[i])
        print(l[(i+1)*-1])
        if l[i] == l[(i + 1) * -1]:
            res = True
        else:
            res = False
            break

    if res == True:
        print("Is Palindrome")
    elif res == False:
        print("Not a Palindrome")







class Main():
    pd([10,23,34,34,23,10])

if __name__ == '__main__':
    Main()

