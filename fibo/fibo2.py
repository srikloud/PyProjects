def fib2(n):
    a, b = 0, 1
    for i in range(0, n):
        a,b = b,a+b
    print(b)

class Main():
    fib2(5)


if __name__ == '__main__':
    Main()
