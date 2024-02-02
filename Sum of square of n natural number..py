
x = int(input("Enter the range: "))
c = 0
for i in range(1, x+1):
    i = i ** 2
    c += i
    i += 1
if x >= 1:
    print(c)
else:
    print('Incorrect input!')


'''
Time Complexity: O(N)
    Space Complexity: O(N)
    
    where 'N' is the given number.
    
def sumOfSquares(n):
    if n == 1:
        return 1

    return sumOfSquares(n - 1) + n * n
'''
'''
Time Complexity: O(N)
    Space Complexity: O(1)

    where 'N' is the given number.
    
def sumOfSquares(n):
    summ = 0

    for i in range(1, n + 1):
        summ += i * i

    return summ
'''
'''
Time Complexity: O(1)
    Space Complexity: O(1)
    
    where 'N' is the given number.
    
def sumOfSquares(n):
    summ = n * (n + 1) * (2 * n + 1) // 6

    return summ
'''