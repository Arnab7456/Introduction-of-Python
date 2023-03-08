'''
Tuple : 

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable

'''

from more_itertools import peekable


thistuple = ("apple", "banana", "cherry")
print(thistuple[2])
print(thistuple)
print(len(thistuple))

#  important thing we cannot create an empty tuple
# but we create a single tuple and ',' important

t=(45,)
print(t[0])

## range test
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:6])


## checking in tupules

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
