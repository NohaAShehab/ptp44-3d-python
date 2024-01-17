
name= 'Nesma Talaat'
""" cast string to a list """
name = list(name)
print(name)  # ['n', 'o', 'h', 'a']
#
#
# newname= 'ahmed'
# newname = list([newname])
# print(newname)  # ['ahmed']


#
# year = 2024
# year = list(year)  # Error , int object is not iterable
# print(year)


# year = 2024
# year = list(str(year))
# print(year)

year = 2024
year = str(year)  # '2024'
# year = list(year) # ['2','0', '2', '4']
# print(year)
year = tuple(year) # ('2','0', '2', '4')
print(year)


""" split string """
message='we love python'
message = message.split(' ')  # return list
print(message)

connect_message = ['we', 'support', 'Hammas', '<3']

""" convert to string  ---> use function .join """
print(connect_message)
connect_message= ' '.join(connect_message)  # join accepts iterable (list, tuple # )
print(connect_message)


state = 'interesting'
state_string='_'.join(state) # string
print(state_string)
# for c in state:
#     print(c)


# info = ['noha', 'iti', 31]
#
# print('_'.join(info))















