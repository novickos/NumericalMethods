import math
#def f(x):
   # return x*x*x+x-1

#def p_f(x):
   # return 3*x*x+1

def f(x):
    return math.exp(x)+2*x+1

def p_f(x):
    return math.exp(x)+2

#def f(x):
 #   return x**3+3*x**2+12*x+8

#def p_f(x):
 #   return 3*x**2+6*x+12


########################################################

def bisekcja(f, a, b, eps):
    if f(a)*f(b)>=0:
        return -1

    x = (a+b)/2
    if f(x) == 0:
        return x
    else:
        while(abs(a-b) > eps):
            x = (a+b)/2
            if(f(x) * f(a) < 0):
                b = x
            elif(f(x) * f(b) < 0):
                a = x

        return (a+b)/2



def nr(f, p_f, x, eps2):
    x1 = x-f(x)/p_f(x)

    if abs(f(x1)) < eps2:
        return x1
    if abs(x1-x) <= eps2:
        return x1

    return nr(f, p_f, x1, eps2)

if __name__ == '__main__':
    eps = 0.01                  #dokladnosc
    eps2 = 1*pow(10,-5)

    print(bisekcja(f, -12, 14, eps))
    print("Newton: " + str(nr(f, p_f, -5, eps)))
