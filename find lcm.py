a = int(input('Enter first number: '))
b = int(input('Enter Second number: '))
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print('The L.C.M of these numbers are: ',b)