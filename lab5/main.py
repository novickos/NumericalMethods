import random

def f(x):
    return 0.3*x*x*x*x-12*x*x+x+5


def prostokat(xp, xk, n):
    dx = (xk-xp)/n
    arr=[xp]

    for i in range(n+1):
        arr.append(arr[i]+dx)

    wynik = 0

    for i in range(1,n+1):
        wynik+=f(arr[i])
    wynik=wynik*dx

    print("metoda prostokatow: " + str(wynik))

def trapez(xp,xk,n):
    dx = (xk-xp)/n
    arr=[xp]             #x0, x1, ..., xn
    wynik = 0

    for i in range(n+1):
        arr.append(arr[i]+dx)

    for i in range(1,n+1):
        wynik+=(f(arr[i-1])+f(arr[i]))/2*dx

    print("metoda trapezow: " + str(wynik))


def simpson(xp,xk,n):
    dx = (xk-xp)/n
    arr=[xp]

    for i in range(n+1):
        arr.append(arr[i]+dx)

    wynik = 0

    for i in range(1,n+1,2):
        wynik += (f(arr[i-1])+4*f(arr[i])+f(arr[i+1]))*dx/3


    print("metoda simpsona: " + str(wynik))



def monte_carlo(xp, xk, n):
    #arr_y=[1.5,2.6,3.8,4.5]
    arr_x=[]
    srednie=0

    for i in range(n):
        arr_x.append(round(random.uniform(xp,xk),1))

    for i in range(n):
        srednie+=f(arr_x[i])/n

    wynik = srednie * abs(xk-xp)

    print("metoda monte carlo: "+ str(wynik))

if __name__ == '__main__':
    xp = 1
    xk = 6
    n = 100000

    prostokat(xp,xk,n)
    trapez(xp,xk,n)
    simpson(xp,xk,n)
    monte_carlo(xp, xk, n)
