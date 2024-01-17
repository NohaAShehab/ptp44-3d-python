
""" define range in python"""

myrange = range(0,5)

print(myrange)

## range object -->

# for item in myrange:
#     print(f"item = {item}")


# counter = 0
# for char in 'python':
#     print(f"{char}: {counter}")
#     counter +=1

# word = 'python'
# for index in range(0,len(word) ):
#     print(index, word[index])


# myr=  range(10)
# print(myr)
#
#
# for i in myr:
#     print(i)


## print chars and its index in anygiven string

msg = 'hello world'
no_of_chars = len(msg)  # 11
# index_range =range(no_of_chars)  ### 0 ---> 10
#
# for abbass in index_range:
#     print(abbass, msg[abbass])

## loop over the range to get the number
# for abbass in range(10):
#     print(abbass)
# #
# for abbass in range(no_of_chars):
#     print(abbass, msg[abbass])



# name = 'reem'
# print(name[2])



#############################################################

# print even number in range 0 to 10

#
# for i in range(10):
#     if i%2==0:
#         print(i)
#


# range(start,stop, step)
for i in range(0,10,2):
    print(i)
#
#
# msg = 'we love python'
# print(msg[::3])
#

msg= 'python is easy'

print(msg.replace(' ',''))


### cast range to a list

# myr = range(0,100, 3)
#
# myl = list(myr)
# print(myl)


""" check this """




# myr = range(100,0, -3)
# myl = list(myr)
# print(myl)


myr = range(0,-100, -3)
myl = list(myr)
print(myl)















