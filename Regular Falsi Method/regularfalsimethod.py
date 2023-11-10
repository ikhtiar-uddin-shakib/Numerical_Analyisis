from math import cos
def f(x):
    return x*3-cos(x)-1
def regfalsi(a,b,e):
    step =1
    print('\n Regular Falsi Method')
    condition = True
    while condition:
        c = ((a*f(b))-(b*f(a)))/(f(b) - f(a))
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
    regfalsi(a,b,e)