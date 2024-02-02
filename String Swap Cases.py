def convert_to_upper(string):
    new = " "
    for i in string:
        j = ord(i) - 32
        if 97 <= ord(i) <= 122:
            new = new + chr(j)
        else:
            new += i
    print(new + '\n')


def convert_to_lower(string):
    new = " "
    for i in string:
        j = ord(i) + 32
        if 65 <= ord(i) <= 90:
            new = new + chr(j)
        else:
            new += i
    print(new + '\n')


def Input(option):
    print(String)
    num = int(input("*"))
    if num == 1:
        convert_to_upper(input("Enter the string: \n"))
        Input(String)
    elif num == 2:
        convert_to_lower(input("Enter the string: \n"))
        Input(String)
    elif num == 3:
        a = input("Enter the string: \n")
        convert_to_upper(a)
        convert_to_lower(a)
        Input(String)
    else:
        print('Wrong Input...Try again! \n')
        Input(String)


String = 'Select any Option: \n 1.Uppercase\n 2.Lowercase\n 3.Both\n'
Input(String)




'''
#upper to lower
string = input("Enter the string: ")
new = ' '
for i in string:
    if 65<=ord(i)<=90:
        i = ord(i) + 32
        new = new + chr(i)
    else:
        new += i
print(new)

#lower to upper
string = input("Enter the string: ")
new = ' '
for i in string:
    if 97<=ord(i)<=122:
        i = ord(i) - 32
        new = new + chr(i)
    else:
        new += i
print(new)
'''