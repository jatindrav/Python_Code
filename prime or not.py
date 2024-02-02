n = int(input('Enter the positive number: '))
b= int(n/2)
is_prime= True
if n==0 and n==1:
    print('It is not a prime number.')
for a in range(2, b):
    if n%a==0 :
        is_prime=False
        break
if is_prime:
    print('is a prime number')
else:
    print('is not a prime number')