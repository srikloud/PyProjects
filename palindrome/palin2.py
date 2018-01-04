def pd(l):
    print(l)
    l2 = []
    for i in range(len(l)):
        l2.append(l[(i+1)*-1])
    print(l2)

    if l == l2:
        print("Is palindrome")
    else:
        print("Not a palindrome")

class Main():
    pd([10,23,34,34,23,10])

if __name__ == '__main__':
    Main()

