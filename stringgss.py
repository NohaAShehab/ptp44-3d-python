
message = 'we love python'

print(type(message))


# 1- get length of the string

print(len(message))  # count all chars in the string including the spaces


# 2- access string parts using index

print(message[4])  # o
print(message[4:])  # ove python
print(message[:4])  # we l

# slicing
print(message[1:9]) # e love p
print(message[::2])


""" 
    write a program that asks the user about his full name 
    print the len of the full name
    if the len > 10 print the chars from 3 to 9 
"""
#write a program that asks the user about his full name
# fullname = input("please enter your full name: ")
# #print the len of the full name
# print(len(fullname))
# # if the len > 10 print the chars from 3 to 9
# if len(fullname) > 10:
#     print(fullname[3:10])



""" count char occurence in the string """

iti = 'information technology institute'

print(iti.count('i'))

# print(len(iti))


""" operations on the string """
""" concat string """
# fname = 'noha'
# lname= 'shehab'
# fullname = fname + ' '+lname
# print(fullname)
#

# fname = 'Nesma'
# lname = 'Talaat'
# fullname = fname +' ' + lname
# print(fullname)
#


# fname = input('Enter first name: ')
# lname = input('Enter last name: ')
# full_name = fname + ' ' + lname
# print(full_name)


# no_of_days = 6 # int
#
# msg = 'Python course duration is ' + str(no_of_days) + ' days'
# print(msg)
#
# print( 'Python course duration is ', no_of_days, 'days')


""" ask the user to enter his name and print welcome message to tis user """
#
# name = input('please enter your name: ')
# if name:
#     mymessage = input("please enter greeting message")
#     # print('please enter greeting : ')
#     greet_messsage =mymessage + name
#     print(greet_messsage)


""" string interpolation """


fname = 'noha'
midname = 'abdelhady'
lanme = 'shehab'

# fullname = fname  + midname + midname + lanme
# print(fullname)
#
# fullname = fname  + midname *2  + lanme
# print(fullname)



""" write a program that ask the user to enter his name and no.of times 
 he want and print the name times equal to this number """


# name = input("please enter your name: ")
# times = input("please enter number of times: ")
# if name and times.isdigit():
#     times = int(times)
#     msg = (name + ' ') * times
#     print(msg)
# else:
#     print("--- Name must be exists and timess must be numbers ")


""" replace """

# msg = 'we love iti'
# newmsg = msg.replace('i', '$') # replace function return new string
# print(msg, newmsg)



# name = 'noha'
# name = name.replace('o', '@')
# print(name)



""" format string """

no_of_students = 13
track_name=  '3d animation'
# track_description = 'We have '+ str(no_of_students) + 'are studying at track '+ track_name
# print(track_description)

## format string

# temp ='We have {0} students are studying at track {1}'
# print(temp)
#
# """format string """
#
# newstring = temp.format(no_of_students, track_name)
# print(newstring)



""" program to greet new users """

# greetmessage = 'Nice to meet you {0}'
# name = input("please enter your name: ")
# customizedmessage = greetmessage.format(name)
# print(customizedmessage)



# name = input('Enter your name: ')
# byear = input('Enter your birth year : ')
#
# if byear.isdigit():
#     byear = int(byear)
#     age = 2024 - byear
#     message = 'Welcome {0} you are now {1} year old'
#     print(message.format(name, age))


""" Yosr Interview """
# name = input('Enter your name: ')
# expected_salary = input("please enter your expected salary: ")
#
# interviewsummary = 'Candidtate with name {0} request average salary of {1}'
# print(interviewsummary.format(name,expected_salary))

# print(interviewsummary.format('noha', 10000))

""" format with keywords"""
# print(interviewsummary.format(expected_salary, name))
#
# interviewsummary = 'Candidtate with name {candidnate} request average salary of {abbass}'
#
# print(interviewsummary.format(abbass=expected_salary, candidnate= name))

# YOu can only concat strings with each others

#################################################################################
""" f-format string """

""" format string based on existing variables """


# name = input("please enter your name: ")
# age = input("please enter your age: ")
#
# info = f"My name is {name}  with {age} years old"
# print(info)





