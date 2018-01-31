from operator import itemgetter
a = [{'b':2},{'b':1},{'b':5},{'b':4}]

print(sorted(a,key=itemgetter('b')))

from operator import itemgetter
a = [{'b':2},{'b':1},{'b':5},{'b':4}]

print(sorted(a,key=itemgetter('b')))

old_dict = {'a': 1, 'c': 3, 'b': 2}

updt_dict = {k:v*10 for k,v in old_dict.items()}
print(updt_dict)