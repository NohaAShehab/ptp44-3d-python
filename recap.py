

width = input("Enter the width: ")
height = input("Enter the height: ")

if width.isdigit():
    width = int(width)
    if height.isdigit()==True:
        height = int(height)
        area = width * height
        print(area)
    else:
        print('height must be an integer')
else:
    print("width must be an integer")