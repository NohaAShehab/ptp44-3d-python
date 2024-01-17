"""
    Ask 5 of your colleagues about their names, and hobbies
and add the info of each one to a list, you should have one list
called colleagues
contains 5 lists


"""

#Ask 5 of your colleagues
no_of_colleagues = 5
colleagues = []
### loop

while no_of_colleagues > 0:
    name=  input("please enter your name: ")
    hoppy = input("please enter your hobby: ")
    #add the info of each one to a list
    info = [name, hoppy]
    colleagues.append(info)
    no_of_colleagues -= 1

print(colleagues)

