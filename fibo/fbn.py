import argparse

def fb_num(n):
    res = input("Enter your name ---")
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Fibonacci number you want to calculate", type=int)

    args = parser.parse_args()

    result = fb_num(args.num)
    print("The Fibonacci number of "+str(args.num)+ " is " + str(result))

if __name__ == '__main__':
    Main()
