import math
a=(int(input('Enter coeficient of x**2: ')))
b= (int(input('Enter coeficient of x: ')))
c=(int(input('Enter constant term: ')))
print(a,'(x)**2 +',b,'(x) +',c)

d= pow(b,2)
sqRoot = math.sqrt(d-4*a*c)

e= -b+sqRoot
f= -b-sqRoot
g= 2*a

root1= e/g
root2= f/g
print('Roots are',root1,root2)
