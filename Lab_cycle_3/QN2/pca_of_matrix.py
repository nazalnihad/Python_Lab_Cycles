import numpy as np


def getMatrix():
    rows = int(input("Enter no of rows : "))
    cols = int(input("Enter no of cols : "))
    matrix = np.empty((rows, cols))

    # creates an empty matrix with given size and inputs the coordinates
    for i in range(rows):
        print(f"Row {i+1}")
        for j in range(cols):
            value = float(input(f"Enter value at [{i+1}][{j+1}] : "))
            matrix[i, j] = value  # assign values to matrix
    return matrix


def find_pca(matrix):

    # finding mean
    mean = np.mean(matrix, axis=0)

    # subract col wise mean from the matrix
    centered_matrix = matrix - mean
    print("\nthe centered matrix is")
    print(centered_matrix)

    # computing covariance matrix of centered_matrix
    covariance_matrix = np.cov(centered_matrix.T)
    print("\nCovariance matrix")
    print(covariance_matrix)

    # computing eigenvectors and eigenvalues of covariance matrix
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    print("\nEigen values")
    print(eigenvalues)

    print("\nEigen vectors")
    print(eigenvectors)

    # compute the projection matrix by finding suitable eigen vectors
    projection_matrix = (eigenvectors.T[:][:2]).T
    P = projection_matrix.T.dot(centered_matrix.T)
    print("\nThe pca of the given matrix is ")
    print(P.T)


mat = getMatrix()
print("\nThe entered matrix is ")
print(mat)
find_pca(mat)
