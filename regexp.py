import re
name = ['cat', 'mat', 'hat', 'pot', 'lot']

for i in range(len(name)):
    if name[i] == ".at":
        print(name[i])

#result = re.search("f", "abcdedf")
#print(result)
result = re.match("a", "abcdedf")
print(result)