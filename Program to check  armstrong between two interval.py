low, high = int(input('Enter 1st interval: ')), int(input('Enter 2nd interval: '))
for n in range(low, high + 1):
    order = len(str(n))
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if n == sum:
        print(n, end=", ")
