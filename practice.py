#                                ----------- list Comprehension-----------------
"""list1=[1,2,3,4,5]
sq_list=[]
for i in list1:
    i=i**2
    sq_list.append(i)
    #print(i)
print("The squared list is: ",sq_list)
print(sq_list[1])"""
# the second solution is the list comprehension method

'''list1=[1,2,3,4,5]
sq_list=[i**2 for i in list1]
print(sq_list)'''

#The traditional for loop method

'''list_natural_num=[1,2,3,4,5,6]
list_natural_num_sq=[]
for i in list_natural_num:
    i=i**2
    list_natural_num_sq.append(i)
print(list_natural_num_sq)'''
# the list comprehension method

"""list_natural_num=[1,2,3,4,5,6]
list_natural_num_sq=[i**2 for i in list_natural_num]
print(list_natural_num_sq)"""
# Filtering items from a list using list comprehension method

"""list_num=[1,2,3,4,5,6]
# we are want find out even numbers from this list
even_num_list=[num  for num in list_num if num%2==0]
print(even_num_list)"""

# Traditional way

"""list_num=[1,2,3,4,5,6]
even_num_list=[]
for num in list_num:
    if num%2==0:
        even_num_list.append(num)
print(even_num_list)"""
# nested list comprehension
"""
matrix=[[1,2],[3,4],[5,6]]
flattened_matrix=[num for row in matrix for num in row ]
print(flattened_matrix)
"""
#Traditional way
"""
matrix=[[1,2],[3,4],[5,6]]
flattened_matrix=[]
for row in matrix:
    for num in row:
        flattened_matrix.append(num)
print(flattened_matrix)
"""
# list comprehension method with multiple conditions
"""
numbers=range(1,20)
filtered_num=[numbers for numbers in numbers if numbers%2==0 and numbers%3==0]
number_filtered=len(filtered_num)
print(f"filered numbers are: {filtered_num}")
print(f"The number of filtered numbers is: {number_filtered}")
"""
# Traditional way
"""
numbers=range(1,20)
filtered_numbers=[]
for num in numbers:
    if num%2==0 and num%3==0:
        filtered_numbers.append(num)
print(filtered_numbers)
"""
# list comprehension method with if_else condition
# Traditional way
"""
list_num=[1,2,3,4,5,6]
# new list will include square of number that's divisible by 2 and cube of numbers that's not
new_list=[]
for num in list_num:
    if num%2==0:
        # here we can comment this line of code bcz we can in append() method
        #num=num**2
        new_list.append(num**2)
    else:
        #num=num**3
        new_list.append(num**3)
print(new_list)
"""
# list comprehension method

"""
list_num=[1,2,3,4,5,6]
new_list=[num**2 if num%2==0 else num**3 for num in list_num]
print(new_list)
"""
# creating tuples of list
"""
coordinates=[(x,y) for x in range(3) for y in range(4)]
print(coordinates)
"""
#Traditional way
coordinates=['x','y']
new_coordinates=[]
for x in range(3):
    for y in range(4):
        new_coordinates.append((x,y))
print(new_coordinates)