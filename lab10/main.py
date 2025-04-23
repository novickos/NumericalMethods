import numpy as np


def LU(n, A):
    L = [[0 for i in range(n)] for j in range(n)]
    U = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        L[i][i] = 0
        for k in range(n):
            sum = 0
            for j in range(i + 1):
                sum += L[i][j] * U[j][k]
            U[i][k] = A[i][k] - sum

        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += L[k][j] * U[j][i]
            L[k][i] = (A[k][i] - sum) / U[i][i]
            print(type(U[i][k]), U[i][k], k, i)
   # print(U)


    y = [0 for i in range(n)]
    for i in range(0, n):
        y[i] = arr[i] / float(L[i][i])
        for k in range(0, i):
            y[i] -= y[k] * L[i][k]

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x, y


def trans(L, n):
    Lt = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            Lt[j][i] = L[i][j]
    return Lt


def Ch(n, A):
    L = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i+1):
            sum = 0
            if (i == j):
                for k in range(j):
                    sum += L[j][k] * L[j][k]
                L[j][j] = pow((A[j][j] - sum), 1 / 2)
            else:
                for k in range(j):
                    sum += L[i][k] * L[j][k]
                L[i][j] = (A[i][j] - sum) / L[j][j]

    y = [0 for i in range(n)]
    for i in range(0, n):
        y[i] = arr[i] / float(L[i][i])
        for k in range(0, i):
            y[i] -= y[k] * L[i][k]

    Lt = trans(L,n)

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= Lt[i][j] * x[j]
        x[i] /= Lt[i][i]

    return x,y




if __name__ == '__main__':
    #A = [[1, 2, 3], [2, 8, 10], [3, 10, 22]]
    #A = [[4, -2, 2], [-2, 2, 2], [2, 2, 14]]
   # A=[[36,30,18,10,12],[30,41,23,3,11],[18,23,14,0,6],[0,-4,6,56,-33],[-3,7,6,-6.6,6.8]]
    A=[[2, -1, 0, 0, 0],
              [-1, 2, -1, 0, 0],
              [0, -1, 2, -1, 0],
              [0, 0, -1, 2, -1],
              [0, 0, 0, -1, 2]]
    n = len(A)
    #arr = [1, 3, 7]
    #arr = [-6, 4, 0]
    arr = [1, 2, 3, 4, 5]
    #arr=[23,3,0,0,9]

    print(LU(n,A))
    #print(Ch(n,A))



def y(n, arr, L):
    y = [0 for i in range(n)]
    for i in range(0, n):
        y[i] = arr[i] / float(L[0][i][i])
        for k in range(0, i):
            y[i] -= y[k] * L[0][i][k]
    return y


def calc_x(n,y, U):
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x
