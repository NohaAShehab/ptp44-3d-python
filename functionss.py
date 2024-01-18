#
# name= 'ahmed'
# print("iti", name, name.upper())
#
# print(len('iti'))
#
# ### define our own functions
#
# # names  = ['Ingy', 'Kareem', 'reem','Tasneem', 'Mohamed', "Aa'laa"]
# #
# # res=names.sort()
# # print(res)
# # names.append('dddd')
# #
# # print(names)
# #
# #
# # message ='we support ghaza'
# # # upper_message = message.upper()
# # # print(upper_message)  # return new string
# #
# # print(message.upper())
#

import  emoji
def sayGoodmorning ():
    print(emoji.emojize("Good morning! :red_heart: :red_heart: :red_heart: ", variant="emoji_type"))


## to call the function
#
# sayGoodmorning()
#
# print("------------------------")


# print("----------------------------------")

# sayGoodmorning()



""" function --> set of lines of code that can accomplish specific task
    --> function can return with result or just do the task (may return with None)
"""


def sayHello():

    return


# sayHello()
#
# sayHello()
#
# x = sayHello()
# print(x)
#




""" sum function s"""
# res = sum([4,5,6,7,7,7,5,5,444,5,5,333])
# print(res)



""" sumnum """

# def sumnum():
#     num1 = input("please enter first number: ")
#     num2 = input("please enter second number: ")
#     if num1.isdigit() and num2.isdigit():
#         num1 = int(num1)
#         num2 = int(num2)
#         res = num1 + num2
#         return res  # stop the function
#     print('--- num1 and num2 must be integers --- ')
#     return
#     print("--- end of the function ---")
#
#
#
# result = sumnum()
# print(result)
#
# print(sumnum())


""""""
def sumnum():
    num1 = input("please enter first number: ")
    num2 = input("please enter second number: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        res = num1 + num2
        return res  # stop the function
    else:
        print('--- num1 and num2 must be integers --- ')
        return


#
# result = sumnum()
# print(result)
#
# print(sumnum())



""" write a function that asks the user to enter his name and display greeting message for him/her

        --> noha 
        
        -> Hi, Noha, Nice to meet you 
"""


# def greet_function():
#     username = input("please enter your Name : ")
#     username = username.capitalize()
#     print(f'Hi , {username}, Nice to meet you')
#
#
# greet_function()
#
#
# greet_function()
#
#
# greet_function()
#
# greet_function()




""" writa a function that ask the user to enter his name and his salary and

    return with the net salary he should earn """


# def ask_for_info():
#     name = input("please enter your name: ")
#     salary = input("please enter your salary: ")
#     if salary.isdigit():
#         salary = int(salary)
#         net_salary = salary *.8
#         print(f"name= {name}, net_sal = {net_salary}")
#
#
# net_sal = ask_for_info()
# print(net_sal)



""" function that accepts argument  """


# print(len())


def sumnumbers(num1, num2):
    res = num1 + num2
    print(res)


sumnumbers(6,6)




def cal_circle_area(dim):
    area = 3.14 * (dim ** 2)
    return  area


print(cal_circle_area(7))









