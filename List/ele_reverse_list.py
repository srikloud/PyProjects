l = ['sri','kanth','chaw','iti']
l3 = list()
l4 = list()
for i in range(0,len(l)):
    l2 = l[i]
    for i in range(0,len(l[i])):
        l3.extend(l2[-1*(i+1)])
    print(l3)
    ll = ''.join(l3)
    l4.append(ll)
    l3 = list()
print(l4)

#list()
#print()
#range()
#len()
#range()
#append()
#extend()
#join()
