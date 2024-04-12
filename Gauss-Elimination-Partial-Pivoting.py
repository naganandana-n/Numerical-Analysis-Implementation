import numpy as np

def gaussElimination(aMatrix, bMatrix):

    #prevent future problems by adding contingencies (ie, check correctness of input)

    if aMatrix.shape[0] != aMatrix.shape[1]:
        print("Error: Matrix A is not square")
        return

    if bMatrix.shape[1] > 1 or bMatrix.shape[0] != aMatrix.shape[0]:
        print("Error: Matrix B is not correct size")
        return

    #initializing necessary variables
    n = len(bMatrix) 
    m = n - 1
    i = 0
    x = np.zeros(n)
    newline = "\n"

    #create augmented matrix through Numpy's concatenate feature, and force data type to float
    augmentedMatrix = np.concatenate((aMatrix, bMatrix), axis=1, dtype=float)
    print(f"The initial augmented matrix is: {newline}{augmentedMatrix}")
    print("Solving for the upper-triangular matrix:")

    #applying gauss elimination with partial pivoting

    while i < n:

        #partial pivoting
        for p in range(i+1, n):
            if abs(augmentedMatrix[i, i]) < abs(augmentedMatrix[p, i]):
                augmentedMatrix[[p, i]] = augmentedMatrix[[i, p]]

        if augmentedMatrix[i, i] == 0.0:
            print("Divide by zero error")
            return 

        for j in range(i+1, n):
            scalingFactor = augmentedMatrix[j][i] / augmentedMatrix[i][i]
            augmentedMatrix[j] = augmentedMatrix[j] - (scalingFactor * augmentedMatrix[i])
            print(augmentedMatrix)
        i = i + 1

    #back subsitution to solve for x
    x[m] = augmentedMatrix[m][n] / augmentedMatrix[m][m]

    for k in range(n - 2, -1, -1):
        x[k] = augmentedMatrix[k][n]

        for j in range(k+1, n):
            x[k] = x[k] - augmentedMatrix[k][j] * x[j]
        
        x[k] = x[k] / augmentedMatrix[k][k]
    
    #displaying the solution
    print(f"The following X matrix solves the above augmented matrix:")
    for answer in range(n):
        print(f"x{answer} is {x[answer]}")

variableMatrix = np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 9, 3, 1, 0, 0, 0],
                           [9, 3, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 25, 5, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 25, 5, 1],
                           [0, 0, 0, 0, 0, 0, 64, 8, 1],
                           [6, 1, 0, -6, -1, 0, 0, 0, 0],
                           [0, 0, 0, 10, 1, 0, -10, -1, 0],
                           [2, 0, 0, 0, 0, 0, 0, 0, 0]])

constantMatrix = np.array([[2],
                           [3],
                           [3],
                           [9],
                           [9],
                           [10],
                           [0],
                           [0],
                           [0]])

gaussElimination(variableMatrix, constantMatrix)