
""" format the string

    any operation on the string returns new string
    -string is immutable data type-
"""

"format string "
""" format function """
name = input("please enter your name: ")
age = input("please enter your age: ")
# if age.isdigit():
#     age = int(age)
temp = 'My name is {0} and I am {1} years old '
print(temp.format(name, age))

""" format function with keyword arguments """
temp2 = 'My name is {username} and I am {userage} years old '
print(temp2.format(username=name ,userage=age))


""" using f format """

temp3 =  f'My name is {name} and I am {age} years old'
print(temp3)