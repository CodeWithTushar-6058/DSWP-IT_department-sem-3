'''
Practical 1:
    Write a program to read a list of elements. Modify this list so that it does not
contain any duplicate elements, i.e., all elements occurring multiple times in the list should
appear only once.
'''


def R_D(input_string):
    unique_list = []
    for element in input_string:
        if element not in  unique_list:
            unique_list.append(element)
    return  unique_list
input_string = input("Enter a list of elements separated by spaces: ").split()
result_list = R_D(input_string)
print("List with duplicates removed:", result_list)
