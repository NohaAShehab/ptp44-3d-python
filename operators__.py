#
# num1 = 10
# num2 = 35
#
#
# res = num1 + num2
#
# print(res)
#
#
# res = num1 **2
# print(res)

#
# num1 = 21
# num2 = 8
#
# res = num1/num2
# print(res)
#
#
# res2 = num1 % num2  # the reminder of the division operator
# print(res2)
#
# res3 = num1 // num2  # division without fraction
# print(res3)


# num = 4
#
# res = num ** 4
# print(res)


# num_= 100
#
# num_ += 50  # num10 = num10 + 50
# print(num_)


# print("====== start ======")
#
name = 'Sara'
print(name=='sara')
if name=='sara':
    print('Nice to meet you sara ')
#
#
#
# print("====== end ======")


# do_you_love_cats = False
#
# if do_you_love_cats == False:
#
#     print("--- Nooooooooooooooooooo ------- ")
#
#
# import emoji
#
# print(emoji.emojize("Python is fun :red_heart::face_with_tears_of_joy::face_with_tears_of_joy::face_with_tears_of_joy:"))
#
#

#
# grade = 65
# print(grade> 80)
# if grade > 80:
#     print("----- Very good ----")


""" input function """

# name = input("please enter your name: ")
# print(name, type(name))

"""

    write a program that asks the user to enter weather temp and display the weather state 
"""

#
# temparture = input("please enter current temperature: ")  # string
# print(temparture, type(temparture))

# print(temparture.isdigit())
# if temparture.isdigit()==True:
#     temparture =int(temparture)
#     print(temparture, type(temparture))
#
# else:
#     print("--- please enter valid temperature  ----")
#



"""--------------------------------"""

# current_temp = input("please enter your current temperature: ")  # string
#
# if current_temp.isdigit() == True:
#     current_temp = int(current_temp)
#     if current_temp > 25:
#         print("--- the weather is hot ")
#     else:
#         print("--- the weather is is cold ")
#
# else:
#     print(""" please enter a valid temperature ---""")
#
#

""" ----------- elif ----------------- """

current_temp = input("please enter your current temperature: ")  # string

if current_temp.isdigit() == True:
    current_temp = int(current_temp)
    if current_temp > 25 and current_temp < 30:
        print("--- the weather is fine ")
    elif current_temp >=30 and current_temp < 40:
        print("---- the weather is is hot ")
    elif current_temp <=25 and current_temp> 20:
        print("----- the weather is cool ")
    elif current_temp <=20:
        print("--- the weather is cold")
    else:
        print("very hot weather ")
else:
    print(""" please enter a valid temperature ---""")



""" 
write a program to ask user to enter a message if he entered 'Hi' ask him about his name  and print it 
otherwise print nice to meet you 

"""

#write a program to ask user to enter a message

user_msg = input("please enter a message: ")

#if he entered 'Hi' ask him about his name  and print it
if user_msg =='Hi':
    username = input("please enter your name: ")
    print(username)

else:
    # print nice to meet you
    print("nice to meet you")























