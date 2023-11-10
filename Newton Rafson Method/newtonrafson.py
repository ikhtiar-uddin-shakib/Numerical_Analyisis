from math import cos,sin

def f(x):
    return x*3-cos(x)-1
    
def f1(x):
    return 3 + sin(x)

def newtonRaphson(x0,e,N):
    print('Newton Rapson Method')
    step = 1
    flag = 1
    condition = True
    while condition:
        if f1(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/f1(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

newtonRaphson(x0,e,N)