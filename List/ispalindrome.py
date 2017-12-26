l = [10,20,30,20,50,10]
l2 = list()

for i in range(1, len(l)+1):
    l2.append(l[-i])
print(l2)

if l == l2:
    print("good")
else:
    print("bad")
