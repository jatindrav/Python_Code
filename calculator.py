print("Select suitable option in next line: ")
print('1: Add')
print('2: Subtract')
print('3: Multiply')
print('4: Divide')
print('5: Remainder')
textinput = int(input('Enter one option: '))

if textinput == 1:
    print('For Addition enter two number: ')
    a, b = float(input()), float(input())
    add = a + b
    print('Ans. ', add)

elif textinput == 2:
    print('For Subtraction enter two number: ')
    a, b = float(input()), float(input())
    sub = a - b
    print('Ans. ', sub)

elif textinput == 3:
    print('For Multiply enter two number: ')
    a, b = float(input()), float(input())
    mul = a * b
    print('Ans. ', mul)

elif textinput == 4:
    print('For Divide enter two number: ')
    a, b = float(input()), float(input())
    div = a / b
    print('Ans. ', div)

elif textinput == 5:
    print('For Remainder enter two number: ')
    a, b = float(input()), float(input())
    rem = a % b
    print('Ans. ', rem)
