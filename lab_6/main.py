def pochodne(arr_x,arr_y):
    k=4
    n=2

    p_ksi = [[0] * k for i in range(n)]
    p_ni = [[0] * k for i in range(n)]
    fun_detj = [[0] * n for i in range(n)]

    waga = [1,1]
    punkt = [-0.577350292,0.577350292]

    #POCHODNE
    for i in range(n):
        p_ksi[i][0] = -0.25*(1-punkt[i])
        p_ksi[i][1] = 0.25*(1-punkt[i])
        p_ksi[i][2] = 0.25*(1+punkt[i])
        p_ksi[i][3] = -0.25*(1+punkt[i])

        p_ni[i][0] = -0.25*(1-punkt[i])
        p_ni[i][1] = -0.25*(1+punkt[i])
        p_ni[i][2] = 0.25*(1+punkt[i])
        p_ni[i][3] = 0.25*(1-punkt[i])
    print(p_ksi)
    print("ur mom")
    print(p_ni)

    #WYZNACZNIK

    for i in range(n):
        for j in range(n):
            dx_dksi = p_ksi[i][0]*arr_x[0] + p_ksi[i][1]*arr_x[1] + p_ksi[i][2]*arr_x[2]+ p_ksi[i][3]*arr_x[3]
            dy_dksi = p_ksi[i][0]*arr_y[0] + p_ksi[i][1]*arr_y[1] + p_ksi[i][2]*arr_y[2]+ p_ksi[i][3]*arr_y[3]

            dx_dni = p_ni[j][0]*arr_x[0] + p_ni[j][1]*arr_x[1] + p_ni[j][2]*arr_x[2]+ p_ni[j][3]*arr_x[3]
            dy_dni = p_ni[j][0]*arr_y[0] + p_ni[j][1]*arr_y[1] + p_ni[j][2]*arr_y[2]+ p_ni[j][3]*arr_y[3]

            fun_detj[j][i] = dx_dksi * dy_dni - dy_dksi * dx_dni


    #POWIERZCHNIA
    powierzchnia=0

    for i in range(n):
        for j in range(n):
            powierzchnia +=abs(fun_detj[j][i])*waga[i]*waga[j]
    print(powierzchnia)


if __name__ == '__main__':
    print('plz no')

    arr_x = []
    arr_y = []


    with open('plik.txt') as file:
        for line in file:
            temp = line.strip().split(',')
            arr_x.append(float(temp[0]))
            arr_y.append(float(temp[1]))

    print(arr_x,arr_y)
    pochodne(arr_x,arr_y)

