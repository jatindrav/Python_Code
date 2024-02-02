a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print('The H.C.F of these numbers are: ',a)