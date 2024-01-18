

# def myfun():
#     return
#
# print("-----------------------")
#
# fun_res= myfun()
# print(fun_res)

### introudce key pass

# def myfunc():
#     return
#
# def emptyfun():
#     pass # null operation
#
#
# fun_res= emptyfun()
# print(fun_res)



#################################################################################

""" write a function that repeatedly asks the user to enter number
until he/she enters valid number otherwise display error message and re ask it
"""


# def askfor_num():
#     while True:
#         num = input("please enter a number: ")
#         if num.isdigit():
#             print(f"thank you for entering number {num}")
#             num = int(num)
#             return num  # out me from the function
#
#         print("------ please enter a valid number ")


# age = askfor_num()
# print(age)



"""  write a function that asks the user to enter his first name and last name and

return with his fullname 
"""


# def get_fullname():
#     firstname = input("please enter first name: ")
#     lastname = input("please enter last name: ")
#     firstname = firstname.capitalize()
#     lastname = lastname.capitalize()
#     fullname = f'{firstname} {lastname}'
#     return  fullname
#
#
# myfullname = get_fullname()
# print(myfullname)


###########################################

""" get and format fullname """

""" function with default argument"""
# def get_format_fullname(first_name, last_name=''):
#     full_name = f'{first_name} {last_name}'
#     # print(full_name)
#     return  full_name.title()
#
#
# myfullname = get_format_fullname("ahmed", 'ali')
# print(myfullname)
#
#
# ###
#
# myname = get_format_fullname("noha")
# print(myname)



# print("ahmed", 'ali', 'mohamed', sep='@', end='$')
# print("Nice to meet you")
#
#
#
# data = [2,4,56,343,4234]
# data.sort(reverse=True)



""" ----------------------------------"""

# def sumnums(num1,num2):
#     print(f"num1 ={num1}, num2 = {num2}")
#     res = num1 + num2
#     print(f"result = {res}")
#
#
#
# sumnums(43,56)
#
# sumnums('Ahmed', 'mohamed')
#
# sumnums("Ahmed", 50)



# def sumnums(num1,num2):
#     print(f"num1 ={num1}, num2 = {num2}")
#     print(f"num1 type= {type(num1)}, num2 type= {type(num2)}")
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         print(f"result = {res}")
#         return res
#     print("--- num1 and num2 must be integers ---")
#
#
#
# sumnums(43,56)
#
# sumnums('Ahmed', 'mohamed')
#
# # sumnums("Ahmed", 50)
# ### isinstance
# print(isinstance(10 , int))
# print(isinstance('Engy', bool))




# num=10
# numtype = type(10)
# print(numtype)
#
# if numtype == int:
#     print("yes")
# else:
#     print("no")
#
#
# print(isinstance(33, bool))



""" example """

""" 

    write the function accepts 3 values 
    check if the the 3 values are integers then multiply them 
    other wise of the values are all strings the  concat them 
    else:
    print error message and
"""

def testfunction(val1, val2, val3):
    if isinstance(val1, int ) and isinstance(val2 , int) and isinstance(val3, int):
        res = val1 * val2 * val3
    elif isinstance(val1, str) and isinstance(val2, str) and isinstance(val3, str):
        res = f'{val1} {val2} {val3}'
    else:
        print('---- ERROR ---- ')
        res= None

    return res

#
# print(testfunction(3,4,5))
# print(testfunction('ahmed', 'mohamed','ali'))
# print(testfunction('ahmed',3 ,'ali'))
#



def testfunction(val1, val2, val3):
    if isinstance(val1, int ) and isinstance(val2 , int) and isinstance(val3, int):
        res = val1 * val2 * val3
        return  res
    elif isinstance(val1, str) and isinstance(val2, str) and isinstance(val3, str):
        res = f'{val1} {val2} {val3}'
        return  res

    print('---- ERROR ---- ')


print(testfunction(3,4,5))
print(testfunction('ahmed', 'mohamed','ali'))
print(testfunction('ahmed',3 ,'ali'))



def testfunction(val1, val2, val3):
    if isinstance(val1, int ) and isinstance(val2 , int) and isinstance(val3, int):
        res = val1 * val2 * val3
    elif isinstance(val1, str) and isinstance(val2, str) and isinstance(val3, str):
        res = f'{val1} {val2} {val3}'
    else:
        res= '----Error ----'

    return res

