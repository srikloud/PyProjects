def permuatations(s):
    if not s:
        yield s
    else:
        for i in range(len(s)):
            r = s[:i]+s[i+1:]
            #print(s[:i])
            print(s[i+1:])


def permute(seq):
    print("0")
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            print("1")
            rest = seq[:i]+seq[i+1:]
            print(rest)
            for x in permute(rest):
                print(rest)
                print("2")
                print("seq[i:i+1]  "+str(seq[i:i+1]))
                print("x "+x)
                yield (seq[i:i+1]+x)

def perm(lst):
    #print('perm def')
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            #print('for')
            x = lst[i]
            print(x)
            xs = lst[:i] + lst[i+1:]
            print(xs)
            for p in perm(xs):
                l.append(x+p)
        return l




#r = list(permute('abc'))
#r = list(permuatations('stack'))
data = 'abc'
for p in perm(data):
    #print('perm')
    print(p)