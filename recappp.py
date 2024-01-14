

# define variable

course = 'Maya'
track = '3DAnimation'
intake = 44
happy = True
g = 9.81
balance =None

# indentation

print(course, track)
print('Hello Ghaza')


# if condition ->


# grade = 60
#
# # if grade >=60:
# #     print("-- Congratulations! You passed the exam")
# # else:
# #     print("-- Unfortunately, you didn't pass the exam")
#
#
# if grade> 85:
#     print("=== Excellent ===")
# elif grade > 75:
#     print("--- Very Good ===")
# elif grade > 65:
#     print("---Good ---")
# elif grade >60:
#     print("=== Pass ====")
# else:
#     print("---- You Failed =====")


""" ask user to enter input """

message= input("please enter your name: ")

print(message, type(message))


age = input("please enter your age: ")

print(age, type(age))

print(age.isdigit())

if age.isdigit()==True:
    age= int(age)
else:
    print("--- age must be an integer")