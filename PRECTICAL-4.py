#PRECTICAL 4
'''
Implement basic operations on arrays.
'''

import array
a = array.array('i',[1,2,3,4])
print("Original Array", a)
# Accessing Elements
print("Accessed element: ", a[0])
#Remove Elements
print("Removed element: ", a.pop())
# update Elements
a[0]=10
print("Updated Array: ", a)
# Append elements
a.append(5)
print("Appended element: ", a)
#Insert element
a.insert(1, 4)
print("Inserted element: ",a)
# Length of array
print("Length of array: ", len(a))
#Iterating Over Elements
for i in a:
 print(i, end=" ")
print()
#Reverse array
a.reverse()
print("Reversed array: ", a)