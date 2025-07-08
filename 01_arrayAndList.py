## Array
from array import *

arr = array("i",[23,56,88,34,67,9,76])

for i in arr:
    print(i,end=" ")

for i in range(len(arr)):
    print(arr[i],end=" ")

"""
array functions 

append()
count()
extend()
fromlist()
index()
insert()
pop()
remove()
reverse()
tolist()

""" 

arr.append(29) ## will append the value at the end of the array
print(arr)

print(arr.count(23)) ##will count how many of the element present in the array

print(arr.index(88)) ##will give the index of the given value

arr.insert(5, 65) ## will insert the value in given index li insert(index, value)
print(arr)

arr.pop(5) ## will delete the element in given index
print(arr)

arr.remove(88) ## will delete the given element
print(arr)

arr.reverse() ## will reverse the whole array
print(arr)

new = arr.tolist() ## will convert the array to list
print(type(new))


"""

Array:
- collection of homogenious datatype
- fixed size (but in python array in resizeble)
- indexed

Dynamic Array
- collection of homogenious datatype
- resizeble
- indexed

List
- collection of hectrogenous datatype
- resizeble
- indexed

"""

### List

l1 = [12, 23, 43]
l2 = []
l3 = [12, 32.43, 'abc']


"""
list functions 

append()
clear()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()

"""
## same as array ##

##builtin methods
# len()
# sum()
# max()
# min()
# sorted()

## difference between list and array
# - list and array both are growable
# - list can contain hectroginous datatype
# - array can contain homogenous datatype

"""
## NOTE

if we want to perform mathemetical calculations, then
we should use NumPy arrays by inpoting NumPy packege

Otherwise use list as it work in a similar way
and more flexible to work with.

_________________Example______________

Installation: pip install numpy

import numpy as np

a = np.array([1,2,3])
print(a)

"""

