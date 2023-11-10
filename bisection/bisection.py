from math import cos
def f(x):
    return x*3-cos(x)-1

def bisection(a,b,e):
    step =1
    print('\n Bisection Method')
    condition = True
    while condition:
        c = (a+b)/2
        print('iteration %d,c= % .2f and f(c)= %.2f' % (step,c,f(c)))
        if f(a) * f(c) <0 :
            b = c
        else:
            a = c
        step = step +1
        condition = abs(f(c))> e
        print('Root : %.2f' % c)
        
a = float(input('first guess: '))
b = float(input('second guess: '))
e = float(input('error: '))

if f(a) * f(b) > 0 :
    print('Given value do not contain root')
else:
    bisection(a,b,e)