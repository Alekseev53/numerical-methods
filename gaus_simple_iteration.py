import numpy as np
from pprint import pprint


def метод_исключения(A, b):
    A = np.array(A, float)
    b = np.array(b, float)
    n = len(b)

    # Прямой ход
    for i in range(n):
        # Приведение к верхнетреугольному виду
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]

    return x


def метод_гаусса_с_выбором(A, b):
    A = np.array(A, float)
    b = np.array(b, float)
    n = len(b)

    # Прямой ход
    for i in range(n):
        # Частичный выбор главного элемента по столбцу
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[[i, max_row]], A[[max_row, i]] = A[[max_row, i]].copy(), A[[i, max_row]].copy()
        b[i], b[max_row] = b[max_row], b[i]

        # Приведение к верхнетреугольному виду
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]

    return x


def метод_гаусса(A, b):
    A = np.array(A, float)
    b = np.array(b, float)
    n = len(b)

    # Прямой ход
    for i in range(n):
        # Приведение к верхнетреугольному виду без выбора главного элемента
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]

    return x


def is_diagonally_dominant(A):
    """Check if matrix A is diagonally dominant."""
    n = len(A)
    for i in range(n):
        if abs(A[i][i]) <= sum(abs(A[i][j]) for j in range(n) if j != i):
            return False
    return True


def метод_простых_итераций(A, b, max_iterations=1000, tol=1e-10):
    if not is_diagonally_dominant(A):
        print("Warning: Matrix A is not diagonally dominant. Convergence might not be guaranteed.")

    n = len(b)
    x = np.zeros(n)
    for _ in range(max_iterations):
        new_x = np.zeros(n)
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            new_x[i] = (b[i] - s1) / A[i][i]

        if np.linalg.norm(new_x - x) < tol:
            return new_x

        if np.any(np.abs(new_x) > 1e50):
            print("Warning: Method seems to be diverging. Stopping iterations.")
            return new_x

        x = new_x
    return x


def метод_зейделя(A, b, max_iterations=1000, tol=1e-10):
    n = len(b)
    x = np.zeros(n)
    for _ in range(max_iterations):
        new_x = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * new_x[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            new_x[i] = (b[i] - s1 - s2) / A[i][i]

        if np.linalg.norm(new_x - x) < tol:
            return new_x

        x = new_x
    return x


# Тестирование
A = [
    [2, 1, 3],
    [1, 3, 2],
    [1, 1, 2]
]
b = [1, 12, 0]

# Defining a new diagonally dominant matrix and vector b
A_diagonal_dominant = [
    [4, 1, 0],
    [1, 3, 1],
    [0, 1, 4]
]
b_diagonal_dominant = [15, 10, 10]

results = {
    "Метод исключения": метод_исключения(A, b),
    "Метод Гаусса с выбором": метод_гаусса_с_выбором(A, b),
    "Метод Гаусса": метод_гаусса(A, b),
    "Метод простых итераций": метод_простых_итераций(A_diagonal_dominant, b_diagonal_dominant),
    "Метод Зейделя": метод_зейделя(A, b)
}
expected_solution = np.array([1, 3, -2])
accuracy = {method: np.linalg.norm(result - expected_solution) for method, result in results.items()}

pprint(results)
pprint(accuracy)

"""
{'Метод Гаусса': array([ 8.,  6., -7.]),
 'Метод Гаусса с выбором': array([ 8.,  6., -7.]),
 'Метод Зейделя': array([ 8.,  6., -7.]),
 'Метод исключения': array([ 8.,  6., -7.]),
 'Метод простых итераций': array([3.375, 1.5  , 2.125])}
{'Метод Гаусса': 9.1104335791443,
 'Метод Гаусса с выбором': 9.1104335791443,
 'Метод Зейделя': 9.11043357879617,
 'Метод исключения': 9.1104335791443,
 'Метод простых итераций': 4.990616194418483}
"""