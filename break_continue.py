#
# for i in range(10):
#     print(f"i= {i}")
#     print("--------------------------------")
#     if i==4:
#         print(f"--- we reached {i} and loop will be broken")
#         break

#### while

# messages = []
# while True:
#     message = input("please leave a message: ")
#     if message=='done':
#         break
#     messages.append(message)
#
#
#
# print(messages)


#
# num = 0

# while True:
#     print(f"--- hiiii {num}")
#
#     if num==10:
#         break
#     num +=1



for num in range(10):
    if num in (4,5,9):
        print("---- the number will not printed, the current iteration will be skip")
        continue
    print(f"num = {num}")



# name = 'nohashehab'  # string
# print(name[::2])

