x = int(input('Enter the number: '))
b=0
y=x
while x!=0:
        a = x%10
        b = b*10 + a
        x//=10
print(b)
if y == b:
    print('This is palindrome.')
else:
    print("This is not palindrome")
