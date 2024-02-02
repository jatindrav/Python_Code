n = int(input("Enter any number: "))
reverse_number = 0
while n != 0:
    remainder = n % 10
    reverse_number = reverse_number * 10 + remainder
    n //= 10
print(f"{reverse_number} is the reverse number.")
