n = int(input('Enter the range: '))
n1 = int(input('Enter the no.: '))
n2 = int(input('Enter the no.: '))
next = n1 + n2
print('fibonacci series', n1, n2)
while next <= n:
    n1 = n2
    n2 = next
    next = n1 + n2
    print(next)
