import re
import os


joinedpath = os.path.join("C:\k8s","config")
print(joinedpath)
print(os.path.join('C:\mypath', 'subfolder'))
print('\one\two\three')
print(r'\one\two\three')
print('\\one\\two\\three')
print('\\')
#print('\')
#print(r'\one\two\three\')
print(r'\one\two\three'+'\ ')

s = "Regular expressions easily explained!"
print("eas" in s)

result = re.search(".nd","A cat and a rat can't be friends.")
print(result)
result = re.search(r".nd","A cat and a rat can't be friends.")
print(result)
result = re.search(".","A cat and a rat can't be friends.")
print(result)
result = re.search(r".","A cat and a rat can't be friends.")
print(result)

result = re.findall(r".nd","A cat and a rat can't be friends.")
print(result)

result = re.findall(r"[A-Z]","A cat and a rat can't be Friends.")
print(result)


# ^(carat) Usage

#Source: https://www.python-course.eu/re.php
#The only other special character inside square brackets (character class choice) is the caret "^". If it is used directly after an opening square bracket, it negates the choice. [^0-9] denotes the choice "any character but a digit". The position of the caret within the square brackets is crucial. If it is not positioned as the first character following the opening square bracket, it has no special meaning.
#[^abc] means anything but an "a", "b" or "c"
#[a^bc] means an "a", "b", "c" or a "^"

result = re.findall(r"[^abc]","A cat and a rat")
print(result)

result = re.findall(r"[a^bc]","A cat and a bat")
print(result)

result = re.findall(r"M[a,e][i,y]er","Maier, Mayer, Meier, Meyer, Mayor, Miyor ")
print(result)


# *(Wildcard/start) Usage
result = re.findall(r"[at*]","A cat and a rat")
print(result)

result = re.findall(r"nd","A, cat, andy, a, rat, canddy")
print(result)

result = re.findall(r"and*y*","A, cat, andyyyyy, a, rat, canddddddy")
print(result)


result = re.findall(r"ra*","A, cat, andy, a, rat, canddy")
print(result)


result = re.findall(r"ra*","A, cat, andy, a, rain, canddy")
print(result)
result = re.findall(r"ra*","A, cat, andy, a, rin, canddy")
print(result)

result = re.findall(r"ra*","A, cat, andy, a, rat, raaat, canddy")
print(result)

#Uasge of '+'

result = re.findall(r"ra+","A, cat, andy, a, rin, canddy")
print(result)

result = re.findall(r"ra+","A, cat, andy, a, rain, canddy")
print(result)

result = re.findall(r"rat+","A, cat, andy, a, rain, raaat, canddy")
print(result)


#Usage of '?'
print("Usage of '?'")
result = re.findall(r"rat?","A, cat, andy, a, rain, raaat, canddy")
print(result)

#Usage of {m}
print("Usage of '{m}'")
result = re.findall(r"ra{2}t?","A, cat, andy, a, raat, raaat, canddy")
print(result)

#Usage of {m,n}
print("Usage of '{m,n}'")
result = re.findall(r"ra{4,5}t?","A, cat, andy, a, raaat, raaaat, canddy")
print(result)


#Usage of A|B
print("Usage of '|'")
result = re.findall(r"[c|r]at?","A, cat, andy, a, rat, raaaat, canddy")
print(result)


'''
l = ["555-8396 Neu, Allison",
     "Burns, C. Montgomery",
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

Allison Neu 555-8396
C. Montgomery Burns
Lionel Putz 555-5299
Homer Jay Simpson 555-7334

[0-9]-[0-9] 

import re

l = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

for i in l:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
    print res.group(3) + " " + res.group(2) + " " + res.group(1)

'''



