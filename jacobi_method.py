## warning
## this is not my code
## i understand and writing after see this page https://www.codesansar.com/numerical-methods/python-program-jacobi-iteration-method.htm

#Jacobi method
def f1 (x,y,z):
    return (17-y+2*z)/20
def f2 (x,y,z):
    return (-18-3*x+z)/20
def f3 (x,y,z):
    return (25-2*x+3*y)/20
# Defining equations to be solved
# in diagonally dominant formc

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Jacobi Iteration
print()
print("Count    x   y   z")
print()
print('\nCount\tx\ty\tz\n')

condition = True
while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    print("{}   {:.4f}  {:.4f}  {:.4f}".format(count,x1,y1,z1))
    print()
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    condition = e1>e and e2>e and e3>e

print()
print("Solution: x={:.4f}, y={:.4f} and z ={:.4f}".format(x1,y1,z1))
print()
print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))
