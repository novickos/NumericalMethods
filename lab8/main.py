import numpy as np
A = [[4.33,-4.43,1.25],
    [-0.76,0.47,-4.31],
	[2.66,1.35,0.51]]

B = [ 2.27, 1.32, 4.6]
n=len(B)

def Reverse(arr):
   new_arr = arr[::-1]
   return new_arr

def swap(arr, s, f):
    if s == f:
        return arr

    help = arr[s]
    arr[s] = arr[f]
    arr[f] = help

    return arr

def swap_col(arr, s, f):
    if s == f:
        return arr
    temp = 0
    for i in range(len(arr)):
        temp = arr[i][s]
        arr[i][s] = arr[i][f]
        arr[i][f] = temp
    return arr
def eli_Gauss_col(row_col, mat):
    tab_x = []
    for k in range(1, row_col):
        max = mat[k-1][k - 1]
        max_idx = k-1
        for l in range(k, row_col):
            if abs(mat[l][k-1]) > abs(max):
                max = mat[l][k-1]
                max_idx = l
        mat = swap(mat, k-1, max_idx)

        for i in range(k, row_col):
            if mat[k - 1][k - 1] == 0:
                return -1
            m = mat[i][k - 1] / mat[k - 1][k - 1]
            for j in range(k - 1, row_col + 1):
                mat[i][j] -= (float(mat[k - 1][j]) * m)

    for i in range(row_col - 1, -1, -1):
        m = mat[i][row_col]
        for j in range(len(tab_x)):
            m -= mat[i][row_col - 1 - j] * tab_x[j]
        if mat[i][i] == 0:
            return -1
        tab_x.append(m / mat[i][i])

    return Reverse(tab_x)

def eli_Gauss_row(row_col, mat):
    tab_x = []
    temp = [i for i in range(row_col)]
    for k in range(1, row_col):
        max = mat[k-1][k - 1]
        max_idx = k-1
        for l in range(k, row_col):
            if abs(mat[k-1][l]) > abs(max):
                max = mat[k-1][l]
                max_idx = l
        mat = swap_col(mat, k-1, max_idx)
        temp = swap(temp, k-1, max_idx)

        if not mat[k-1][max_idx]:
            return -1

        for i in range(k, row_col):
            m = mat[i][k - 1] / mat[k - 1][k - 1]
            for j in range(k - 1, row_col + 1):
                mat[i][j] -= (float(mat[k - 1][j]) * m)

    for i in range(row_col - 1, -1, -1):
        m = mat[i][row_col]
        for j in range(len(tab_x)):
            m -= mat[i][row_col - 1 - j] * tab_x[j]
        tab_x.append(m / mat[i][i])

    tab_x = Reverse(tab_x)

    for i in range(row_col):
        swap(tab_x, temp.index(i), i)
        swap(temp, temp.index(i), i)

    return tab_x










def swap(A, B, i, j):
	for k in range(n):
		temp = A[i][k]
		temp2 = B[i]

		A[i][k] = A[j][k]
		B[i] = B[j]

		A[j][k] = temp
		B[j] = temp2

		print(B[i], A[i][k])

	print('\n'+"macierz a i b")
	print(A)
	print(B)

def twojastara(A,B):
	for k in range(n):
		max_i = 0
		max_value = A[max_i][0]
		print(B)
		for i in range(k + 1, n):
			if (abs(A[i][k]) > max_value):
				max_value = A[i][k]
				max_i = i
		if (max_i != k):
			swap(A, B, k, max_i)

		#forward tutaj


def forward(A,B):
	for k in range(n-1):
		for i in range(k+1,n):
			m = A[i][k]/A[k][k]
			for j in range(k,n):
				A[i][j] = A[i][j] - m * A[k][j]
			B[i] = B[i] - m * B[k]
	#return -1

def back(A,B):
	x = np.zeros(n,float)
	x[n-1] = B[n-1]/A[n-1][n-1]
	for i in range(n-2,-1,-1):
		temp = B[i]
		for j in range(i+1, n):
			temp = temp - A[i][j] * x[j]
		x[i] = temp/A[i][i]
	return x

def elim_gauss(A,B):
	forward(A,B)
	print(back(A,B))
	print(twojastara(A,B))

	#tu ma printowac ze moze miec nieskonczona ilosc rozwiazan


##################################################################
def elim_gauss_b4(A,B):
    n = len(B)
    x = np.zeros(n,float)

#forward
    for k in range(n-1):
        for i in range(k+1,n):
            m = A[i][k]/A[k][k]
            for j in range(k,n):
                A[i][j] = A[i][j] - m * A[k][j]
            B[i] = B[i] - m * B[k]

#back
    x[n-1] = B[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        temp = B[i]
        for j in range(i+1, n):
            temp = temp - A[i][j] * x[j]
        x[i] = temp/A[i][i]

    return x


if __name__ == '__main__':

	mat = [[-2, -4, 5, -2, -5],
		   [6.5, 2, 1.25, 3.5, 1.75],
		   [1.75, 7.25, -8.75, 5.5, 5],
		   [3.25, -2.75, -3.75, 1, 6]]
	print(eli_Gauss_row(4, mat))
	mat = [[-2, -4, 5, -2, -5],
		   [6.5, 2, 1.25, 3.5, 1.75],
		   [1.75, 7.25, -8.75, 5.5, 5],
		   [3.25, -2.75, -3.75, 1, 6]]
	print(eli_Gauss_col(4, mat))
#    print(elim_gauss(A,B))




















N = 3

# function to get matrix content
def gaussianElimination(mat):

	# reduction into r.e.f.
	singular_flag = forwardElim(mat)

	# if matrix is singular
	if (singular_flag != -1):

		print("Singular Matrix.")

		# if the RHS of equation corresponding to
		# zero row is 0, * system has infinitely
		# many solutions, else inconsistent*/
		if (mat[singular_flag][N]):
			print("Inconsistent System.")
		else:
			print("May have infinitely many solutions.")

		return

	# get solution to system and print it using
	# backward substitution
	backSub(mat)

# function for elementary operation of swapping two rows
def swap(mat, i, j):

	for k in range(N + 1):

		temp = mat[i][k]
		mat[i][k] = mat[j][k]
		mat[j][k] = temp

# function to reduce matrix to r.e.f.
def forwardElim(mat):
	for k in range(N):

		# Initialize maximum value and index for pivot
		i_max = k
		v_max = mat[i_max][k]

		# find greater amplitude for pivot if any
		for i in range(k + 1, N):
			if (abs(mat[i][k]) > v_max):
				v_max = mat[i][k]
				i_max = i

		# if a principal diagonal element is zero,
		# it denotes that matrix is singular, and
		# will lead to a division-by-zero later.
		if not mat[k][i_max]:
			return k # Matrix is singular

		# Swap the greatest value row with current row
		if (i_max != k):
			swap(mat, k, i_max)

		for i in range(k + 1, N):

			# factor f to set current row kth element to 0,
			# and subsequently remaining kth column to 0 */
			f = mat[i][k]/mat[k][k]

			# subtract fth multiple of corresponding kth
			# row element*/
			for j in range(k + 1, N + 1):
				mat[i][j] -= mat[k][j]*f

			# filling lower triangular matrix with zeros*/
			mat[i][k] = 0

		# print(mat);	 //for matrix state

	# print(mat);		 //for matrix state
	return -1

# function to calculate the values of the unknowns
def backSub(mat):

	x = [None for _ in range(N)] # An array to store solution

	# Start calculating from last equation up to the
	# first */
	for i in range(N-1, -1, -1):

		# start with the RHS of the equation */
		x[i] = mat[i][N]

		# Initialize j to i+1 since matrix is upper
		# triangular*/
		for j in range(i + 1, N):

			# subtract all the lhs values
			# except the coefficient of the variable
			# whose value is being calculated */
			x[i] -= mat[i][j]*x[j]

		# divide the RHS by the coefficient of the
		# unknown being calculated
		x[i] = (x[i]/mat[i][i])

	#print("\nSolution for the system:")
	#for i in range(N):
		#print("{:.8f}".format(x[i]))

# Driver program

# input matrix
mat = [[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]]
gaussianElimination(mat)

