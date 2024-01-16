

""" perform this examples

    1- create a new list contains the courses you finished till now
    2- print the len of the list
    3- add the course 'python for maya' to the list using 2 ways
    4- add another list contains subtask to the previous created list
"""

#    1- create a new list contains the courses you finished till now

courses_list = ['python', 'maya', 'english', 'digital painting']
print(len(courses_list))


# 3- add the course 'python for maya' to the list using 2 ways
courses_list.append('python for maya')
print(courses_list)

courses_list.insert(1, 'python for maya')
print(courses_list)

#4- add another list contains subtask to the previous created list
subtasks = ['eat', 'pray', 'sleep', 'walk']
courses_list.append(subtasks)

