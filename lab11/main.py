import math


# def f(x, y):
#   return y

def f(x, y):
    # f = -2 * y + x**3.0 * math.exp(-2*x)
    #f = math.cos(x) - math.sin(x) - y
    f = x+y
    return f


def euler(n, y, x, h):
    for i in range(1, n + 1):
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])
        x[i] = x[i - 1] + h
        print(y[i], x[i])
    return x, y


def heun(n, y, x, h):
    for i in range(1, n + 1):
        wtf = f(x[i - 1], y[i - 1]) + f(x[i - 1] + h, y[i - 1] + h * f(x[i - 1], y[i - 1]))
        y[i] = y[i - 1] + h / (2 * wtf)
        x[i] = x[i - 1] + h
        print(y[i], x[i])
    return x, y

def RK4(x,y,h,n):
    k=[0 for i in range(4)]
    for i in range(1,n+1):
        k[0] = h*f(x[i-1],y[i-1])
        k[1] = h*f(x[i-1]+0.5*h,y[i-1]+0.5*k[0])
        k[2] = h*f(x[i-1]+0.5*h,y[i-1]+0.5*k[1])
        k[3] = h*f(x[i-1]+h,y[i-1]+k[2])
        y[i] = y[i-1]+(k[0]+2*k[1]+2*k[2]+k[3])/6
        print(k, y[i])
    return y


if __name__ == '__main__':
    print("ur mom")
    x0 = 0.0
    b = 0.2
    y0 = 1.0
    h = 0.1

    n = round((b - x0) / h)
    print(n)

    y = [0 for i in range(n + 1)]
    x = [0 for i in range(n + 1)]
    y[0] = y0
    x[0] = x0

    # euler(n,y,x,h)
    #heun(n, y, x, h)
    RK4(x,y,h,n)
