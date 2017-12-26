lst = [10, 5, 2, 7, 4, 9, 12, 1, 15]


l = list()
r = list()
#print(len(lst))
#print(len(list)//2)

for i in range(0, (len(lst)//2)):
     l.append(lst[i])
print(l.__len__())
print(len(l))

for i in range((len(lst)//2), len(lst)):
    r.append(lst[i])
print(r)
