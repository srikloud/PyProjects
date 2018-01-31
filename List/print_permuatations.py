def print_permutations(s):
    str1 = s
    str2 = 'srikanth'
    l = list(str1)
    ll2 = list(str2)
    perm(s)

one = []
two = []


def perm(str1):
    ll_str = [str1[i:] + str1[:i] for i in range(0, len(str1))]
    for i in ll_str:
        # one.append(i)
        for j in range(1, len(i)):
            one.append(i[j:])
        print("one")
        print(one)
        perm2(one)


def perm2(one_t):
    for i in one_t:
        if len(i) > 1:
            t = [i[j:] + i[:j] for j in range(0, len(i))]
            two.append(t)






print_permutations('abcd')