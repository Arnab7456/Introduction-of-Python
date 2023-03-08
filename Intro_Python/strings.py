### lets discuss about string ###
from dataclasses import dataclass


Name = "arnab "
print(Name)
name = '''Arnab
            das'''
print(name)
print(type(name))
 ##concatination in python

print(Name + name)

# in python there is no concept of index out of bound 

## slicing in python ##
## index printing

data = "hello arnab"
print(data[0:14])
print(data[:14])
print(data[0:])

# python strings skipping

data1 = "Arnab"
d1 = data1[1:5:2]
print(d1)