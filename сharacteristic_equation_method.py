import numpy as np

def gaussian_elimination(A, b):
    """
    Решает систему линейных уравнений Ax = b с помощью метода Гаусса.
    
    Параметры:
    - A (numpy.ndarray): Матрица системы
    - b (numpy.ndarray): Вектор правой стороны
    
    Возвращает:
    - numpy.ndarray: Решение системы
    """
    n = len(b)
    M = A.copy()
    i = 0
    j = 0

    while i < n and j < n:
        # Find pivot in column j
        maxval = abs(M[i][j])
        pivot_row = i
        for k in range(i + 1, n):
            if abs(M[k][j]) > maxval:
                maxval = abs(M[k][j])
                pivot_row = k
        if M[pivot_row][j] == 0:
            j += 1
        else:
            # Swap rows
            M[[i, pivot_row]] = M[[pivot_row, i]]
            b[[i, pivot_row]] = b[[pivot_row, i]]
            for k in range(i + 1, n):
                factor = M[k][j] / M[i][j]
                M[k, i:] = M[k, i:] - factor * M[i, i:]
                b[k] -= factor * b[i]
            i += 1
            j += 1

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(M[i, i + 1:], x[i + 1:])) / M[i, i]

    return x


def find_eigenvectors(matrix, eigenvalues):
    """
    Находит собственные векторы n x n матрицы для данного собственного значения.
    
    Параметры:
    - matrix (numpy.ndarray): n x n матрица
    - eigenvalues (numpy.ndarray): Собственные значения матрицы
    
    Возвращает:
    - numpy.ndarray: Собственные векторы матрицы
    """
    eigenvectors = []
    
    for lambda_ in eigenvalues:
        # For each eigenvalue, compute the eigenvector using Gaussian elimination
        A_minus_lambdaI = matrix - lambda_ * np.identity(len(matrix))
        b = np.zeros(len(matrix))
        b[-1] = 1
        eigenvector = gaussian_elimination(A_minus_lambdaI, b)
        eigenvector[-1] = 1
        
        # Normalize the eigenvector
        eigenvector = eigenvector / np.linalg.norm(eigenvector)
        eigenvectors.append(eigenvector)
    
    return np.array(eigenvectors)


def find_eigenvalues_and_eigenvectors(matrix):
    """
    Находит собственные значения и собственные векторы n x n матрицы.
    
    Параметры:
    - matrix (numpy.ndarray): n x n матрица
    
    Возвращает:
    - eigenvalues (numpy.ndarray): Собственные значения матрицы
    - eigenvectors (numpy.ndarray): Собственные векторы матрицы
    """
    eigenvalues = np.linalg.eigvals(matrix)  # Getting eigenvalues using numpy for demonstration
    eigenvectors = find_eigenvectors(matrix, eigenvalues)
    return eigenvalues, eigenvectors


# Testing
matrix_test = np.array([[2, -1, 0], 
                        [-1, 2, -1], 
                        [0, -1, 2]])
eigenvalues_test, eigenvectors_test = find_eigenvalues_and_eigenvectors(matrix_test)

# Comparing with numpy's results
eigenvalues_np, eigenvectors_np = np.linalg.eig(matrix_test)

print(eigenvalues_test, eigenvectors_test, eigenvalues_np, eigenvectors_np)
