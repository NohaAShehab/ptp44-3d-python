

# # course = 'maya'
# #
# # print(bool(course))
#
# commission = -100
# print(bool(commission))
#
#
# msg = '                                             '
# print(bool(msg))
#
#
# speech =''
# print(bool(speech))

#
# pii = 0.0
# print(bool(pii))



# pii = "0.0"
# print(bool(pii))

""" ============= Truly or falsy values """


# msg = input("please leave a message: ")
# if msg:
#     print('hii',msg, type(msg))
# else:
#     print('== bye ')

#
# age = input("please enter your age: ")
#
# if age.isdigit():
#     age= 10 * int(age)
#     print(age)
# else:
#     print("-- please enter valid age ==")
#
#
# name = 'mai'
# if name:
#     print('hi')
# else:
#     print('bye')



# print("ahmed" and "iti" and '3d animation')  # 3d animation ---> represent True
#
# print('ahmed' and False and 'ali' and 'iti')   # False
#
#
# print('ahmed' and 'iti' and '' and 'iti' and 'test')  # ''
#
#
#
#
# print(0 or 'maya' or 'python' or 'iti' or False )
#
#
# print(not 'python')
#
# print(not False)


### check this example
#
# width  =input('please enter width: ')
# height =input('please enter height: ')
#
# #
# if width.isdigit() and height.isdigit():
#     # width = int(width)
#     # height = int(height)
#     area = int(width) * int(height)
#     print(area)
# else:
#     print('---- width and height must be numbers ----')
#
#


name = input("please enter your name: ")

# if name:
#     print("-- thank you for entering your name")
# else:
#     print("--- please enter your name:")
################################################################33
if not name:
    print("--- You must enter your name: ")
# else:
#     print("hiii")