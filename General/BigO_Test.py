
# Test Big O(N)

O(1) (worst case): Given the page that a business's name is on and the business name, find the phone number.

O(1) (average case): Given the page that a person's name is on and their name, find the phone number.

O(log n): Given a person's name, find the phone number by picking a random point about halfway through the part of the book you haven't searched yet, then checking to see whether the person's name is at that point. Then repeat the process about halfway through the part of the book where the person's name lies. (This is a binary search for a person's name.)

O(n): Find all people whose phone numbers contain the digit "5".

O(n): Given a phone number, find the person or business with that number.

O(n log n): There was a mix-up at the printer's office, and our phone book had all its pages inserted in a random order. Fix the ordering so that it's correct by looking at the first name on each page and then putting that page in the appropriate spot in a new, empty phone book.

import time
l = list()
for i in range(0,100000):
    l.append(i)
print(time.time())
for i in range(0,len(l)):
    if l[i] == 20000:
        print(l[i])
print(time.time())

print(time.time())
for i in range(0,len(l)):
    if l[i] == 30000:
        print(l[i])
print(time.time())

# Test Big O(N square)
print("Big O(N2)")
ll = list()
for i in range(0,1000):
    l.append(i)
for j in range(0,1000):
    ll.append(j)

print(time.time())
for k in l:
    for m in ll:
        if k == m:
            if l[k] == ll[m]:
                x = 'hello'
print(time.time())

