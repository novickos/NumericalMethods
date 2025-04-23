
def aproksymacja(size, arr_x,arr_y):
    xy = 0
    x = 0
    xpow = 0
    ypow = 0
    y = 0

    for i in range(size):
        xy += arr_x[i]*arr_y[i]
        x += arr_x[i]
        y += arr_y[i]
        xpow += arr_x[i] * arr_x[i]
        ypow += arr_y[i]*arr_y[i]

    a1 = size*xy-x*y
    a1 = a1/(size*xpow - x*x)

    a0 = y*xpow-x*xy
    a0 = a0/(size*xpow - x * x)

    r = size*xy-x*y
    r = r/(((size * xpow - x*x)**(1/2))*((size * ypow - y * y)**(1/2)))

    print("y = " + str(a1) + "x + " + str(a0))
    print("r = " + str(r))
    #return a1, a0, r


if __name__ == '__main__':
    arr_x = []
    arr_y = []

    with open('plik.txt') as file:
        for line in file:
            temp = line.strip().split(',')
            arr_x.append(float(temp[0]))
            arr_y.append(float(temp[1]))

    size = len(arr_x)
    print(arr_x,arr_y)
    aproksymacja(size,arr_x,arr_y)
