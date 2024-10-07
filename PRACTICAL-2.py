#PRECTICAL 2
''' 
Build a program to count the frequency of words
appearing in a string using a dictionary.

'''

d={}
str=input("enetr a string=")
roll=str.split(" ")
print(str)
for i in roll:
    n=roll.count(i)
    print(n)
    d[i]=n
print(d)

