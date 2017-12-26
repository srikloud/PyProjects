l=[3,5,23,6,2,64,10,34]
l_odd = list()
l_even = list()
# Print Odd Numbers
for i in range(0,len(l)):
    print(l[i])
    if l[i]%2 > 0:
        #print("odd")
        l_odd.append(l[i])
    else:
        l_even.append(l[i])
        #print("even")
print("odd")
print(l_odd)
print("even")
print(l_even)