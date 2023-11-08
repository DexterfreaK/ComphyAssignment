


import inspect
import math

def f1(x):
    return x**x + x - 4

def f1prime(x):
    return x**x*(math.log(x) + 1) + 1

def f2(x):
    return 3*x - math.cos(x) - 1

def f2prime(x):
    return 3 + math.sin(x)

def f3(x):
    return x**2 - math.log(x) - 2

def f3prime(x):
    return 2*x - 1/x

def f4(x):
    return x**3 + x**2 + x + 7

def f4prime(x):
    return 3*x**2 + 2*x + 1

def newtonRaphson(x0,f,fprime):

    h = f(x0) / fprime(x0)
    new_x = x0 - h

    print("\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***")
    print("Function: ",inspect.getsource(f),"\nDerivative: ",inspect.getsource(fprime),"\n")
    
    print("Iteration ",1," x = ","%.9f"% new_x)

    for i in range(1,10):

        h = f(new_x) / fprime(new_x)
        new_x = new_x - h
        
        print("Iteration-",i+1," x1 = ","%.9f"% new_x)
        
x0 = 1
newtonRaphson(x0,f1,f1prime)
newtonRaphson(x0,f2,f2prime)
newtonRaphson(x0,f3,f3prime)
newtonRaphson(x0,f4,f4prime)


