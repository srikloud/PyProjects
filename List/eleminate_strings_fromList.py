l = ['sri',1,3,'kanth',4,6,'chaw']
l2 = list()
l3 = list()

for i in range(0,len(l)):

    if str(l[i]).isnumeric():
        l2.append(l[i])
    else:
        l3.append(l[i])
print(l2)
print(l3)


#print(str(l[0]).isnumeric())

