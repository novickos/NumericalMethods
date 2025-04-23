import numpy

#W(x) = y[0][0]+ nawiasy okragle * divided[0][i]

def calc(i, x, arr_x):
    total = 1
    for t in range(i):
        total = total * (x - arr_x[t])
    return total


def newton(size, arr_x, arr_dx, x):
    total = arr_dx[0][0]
    for i in range(1, size):
        total = total + (arr_dx[0][i] * calc(i, x, arr_x))
    return total


def divide(size, arr_x, arr_y):
    arr = numpy.zeros([size, size])
    arr[:, 0] = arr_y
    print(arr)

    for k in range(1, size):
        for i in range(size - k):
            arr[i][k] = (arr[i+1][k-1] - arr[i][k-1]) / (arr_x[i+k] - arr_x[i])
            print("k: " + str(k) + " i: " + str(i) + " arr: " + str(arr[i][k]))
        print("\n")
    return arr

def insertion_sort(arr_x, arr_y):
    n = len(arr_x)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr_x[i]
        key2 = arr_y[i]
        j = i-1
        while j >= 0 and key < arr_x[j]:
            arr_x[j + 1] = arr_x[j]
            arr_y[j + 1] = arr_y[j]
            j -= 1
        arr_x[j + 1] = key
        arr_y[j+1] = key2

if __name__ == '__main__':
    arr_x = []
    arr_y = []

    with open('plik.txt') as file:
        for line in file:
            temp = line.strip().split(',')
            arr_x.append(float(temp[0]))
            arr_y.append(float(temp[1]))

    q = input("Chcesz wstawic nowy punkt? Y/N: ").upper()
    if q == "Y":
        n = int(input("Ile punktów chcesz wstawić? "))
        for i in range(n):
            new_x = (float(input("Podaj nowy x: ")))
            new_y = (float(input("Podaj nowy y: ")))

            if new_x not in arr_x:
                arr_x.append(new_x)
                arr_y.append(new_y)
            else:
                print("Ten punkt już istnieje.")

    insertion_sort(arr_x, arr_y)

    print("X: ")
    print(arr_x)
    print("Y: ")
    print(arr_y, end='\n\n')

    size = len(arr_x)
    x = 1

    arr_dx = divide(size, arr_x, arr_y)
    print(arr_dx)


    print("Wielomian interpolacyjny dla punktu x = "+ str(x) + ": " + str(newton(size, arr_x, arr_dx,x)))
    print("Wielomian interpolacyjny dla punktu x = -3: "+ str(newton(size, arr_x, arr_dx,-3)))
    print("Wielomian interpolacyjny dla punktu x = 1.5: "+ str(newton(size, arr_x, arr_dx,1.5)))
    print("Wielomian interpolacyjny dla punktu x = 55: "+ str(newton(size, arr_x, arr_dx,55)))



