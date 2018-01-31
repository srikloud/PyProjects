def permute(seq):
    print("seq "+seq)
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            print("outer")
            rest = seq[:i]+seq[i+1:]
            print(rest)
            for x in permute(rest):
                print("inner")
                yield seq[i:i+1]+x

r = list(permute('stack'))
print(r)