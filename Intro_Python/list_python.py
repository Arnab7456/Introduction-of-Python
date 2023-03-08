import this


a = [1 , 2 ,4 , 5 , 96, 145]
print(a)
print(a[2])
# index out of range error

# print(a[7])

# lets change value on index

# changeing in first occurence -->
a[0]=45
print(a)

# changeing in last occurence -->
a[5] = 56
print(a)

listcase = [1 , 48 , 7 , 45 , 5 , 12]
list1 = listcase.sort()
print(listcase)


## add something in a list

thislist = ["apple", "banana", "cherry"]
thislist.append("watermealon")
print(thislist)

# here we remove something
thislist.remove("apple")
print(thislist)
print("remove part index  :",thislist.pop(2))
print(thislist)

intcase = [1 , 48 , 7 , 45 , 5 , 12]

intcase.pop(2)
print(intcase)

### sometimes we use del keyword alse
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

## lets .clear all list in python

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
