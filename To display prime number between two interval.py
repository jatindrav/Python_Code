is_prime = True
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('prime numbers between', a, 'and', b, 'are: ')
while a < b:
    is_prime = True
    if a == 0 or a == 1:
        is_prime = False
    c= int(a/2)
    for i in range(2, c):
        i += 1
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
        print(a)
    a += 1
