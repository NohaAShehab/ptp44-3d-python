

# coursename = 'python'
#
#
# for mychar in coursename:
#     print(f"{mychar}")

""" print char and each index """
# coursename=  'python'
# index = 0
# for mychar in coursename:
#     print(f"{index} ..... {mychar}")
#     index +=1


# name = 'mohamed'
#
# # for character in name:
# #     print(f"char = {character}")
#
# for abbass in name:  # abbass is a variable -->
#     print(f"{abbass}")

# print index of eacch char

# name = 'ahmed'
# mycounter =  0
#
# for myvar in name:
#     print(f'{mycounter}: {myvar}')
#     mycounter += 1



""" write a program that prints the number of vowels in a string """

anystring = input("please input a string: ")
no_of_vowels = 0
for abbbass in anystring:
    if abbbass=='a' or abbbass=='e' or abbbass=='o' or abbbass=='i' or abbbass=='u':
        no_of_vowels+=1   # no_of_vowels = no_of_vowels + 1
#
#
#
# print(no_of_vowels)
# print(f"total number of vowels in {anystring} = {no_of_vowels}")


""" 
    write a program that asks the user to enter a string  count number of M or N or S or A appeared any any string 

"""



anystring= input("Please enter a string: ")

# no_of_chars = 0
# for abbasss in anystring:
#     if abbasss.upper()=='M' or abbasss.upper()=='N' or abbasss.upper()=='A' or abbasss.upper()=='S':
#         no_of_chars +=1
#
#
# print(f"Chars M/N/S/A appreared {no_of_chars} time in {anystring}")



no_of_chars = 0
for abbasss in anystring.upper():
    if abbasss=='M' or abbasss=='N' or abbasss=='A' or abbasss=='S':
        no_of_chars +=1


print(f"Chars M/N/S/A appreared {no_of_chars} time in {anystring}")





