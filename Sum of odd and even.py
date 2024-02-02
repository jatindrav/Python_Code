n = int(input("Enter the number:"))
sum_even = 0
sum_odd = 0
while n>0:
    rem = n%10
    n = n//10
    if rem%2 == 0:
        sum_even+=rem
    else:
        sum_odd+=rem
print(sum_even, sum_odd)