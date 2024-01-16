

"1- define a list "
myl = []
mynl = list()
newlist =['book', 'pen', 15, 9.8, True, 'jacket', 'iti', 'jacket','iti', 'jacket']
print(newlist)

"""1- get len of list """
print(len(newlist))

""" count element occurence in the list """

print(newlist.count('iti'))

""" check element exists or not in the list """
print("noha" in newlist)

if 'noha' in newlist:
    print("--- found")
else:
    print("-- not found ")


""" access element using index """
print(newlist)
print(newlist[6])

""" list is mutable data type """
newlist[6] = 'updated'
print(newlist)

# newlist[100]= 'my item'  #IndexError: list assignment index out of range


""" add element to the list """
""" 1.1 append element """

newlist.append('Ingy')
print(newlist)

"""1.2 insert element  """
# newlist.insert(0, 'Yosr')
# print(newlist)

""" mylist.insert(0,'yosr')"""

newlist.insert(1000, 'Ingy')
print(newlist)


""" remove element  from list """
poppped_element=newlist.pop()  # pop element at the end of list and return with the popped element
print(poppped_element)
print(newlist)

""" pop element at certain index """

poppped_element2 = newlist.pop(3)
print(poppped_element2)
print(newlist)

""" remove specific element """
newlist.remove('jacket')  # remove first occurence of the element
print(newlist)

""" loop over the list """
#
# for element in newlist:
#     print(f"element= {element}")


# for element in newlist:
#     if element=='jacket':
#         # newlist.remove('jacket')
#         newlist.remove(element)

    # print(f"{element},  {newlist}")


""" print index of each element in the list """


index = 0

# for element in newlist:
#     print(f"index= {index},element = {element}")
#     index += 1



"""list can hold another list """


# tasks= ['python', 'maya', ['Gym', 'buying', 'sleeping'], 'pray', 'iti', 'money', 'CRY']
# print(tasks[2][2])





""" perform this examples 

    1- create a new list contains the courses you finished till now
    2- print the len of the list 
    3- add the course 'python for maya' to the list using 2 ways 
    4- add another list contains subtask to the previous created list 


"""




















