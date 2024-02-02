def count(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


n = int(input('Enter the no.: '))
print(count(n), "Digit number.")
on = n
power = count(n)
d = 0
c = 0
while n != 0:
    b = n % 10
    c = b ** power
    d += c
    n = n // 10
print(d)
if d == on:
    print('This is armstrong number.')
else:
    print('This is not a armstrong number.')
