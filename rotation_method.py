import numpy as np

def jacobi_rotation(A, tol=1e-10, max_iterations=1000):
    def max_off_diagonal_element(matrix):
        """Найти максимальный элемент матрицы вне диагонали."""
        # Исключаем диагональ, заполнив ее нулями
        modified_matrix = matrix.copy()
        np.fill_diagonal(modified_matrix, 0)
        
        i, j = np.unravel_index(np.argmax(np.abs(modified_matrix)), matrix.shape)
        return i, j, modified_matrix[i, j]

    def compute_phi(matrix, i, j):
        """Вычислить угол поворота фи."""
        if matrix[i, i] == matrix[j, j]:
            phi = np.pi / 4
        else:
            phi = 0.5 * np.arctan(2 * matrix[i, j] / (matrix[i, i] - matrix[j, j]))
        return phi
    
    def jacobi_matrix(matrix, i, j, phi):
        """Построить матрицу поворота Якоби."""
        J = np.eye(matrix.shape[0])
        J[i, i] = J[j, j] = np.cos(phi)
        J[i, j] = -np.sin(phi)
        J[j, i] = np.sin(phi)
        return J

    n = A.shape[0]
    iter_count = 0

    while iter_count < max_iterations:
        i, j, max_val = max_off_diagonal_element(A)

        # Проверка сходимости
        if abs(max_val) < tol:
            break

        phi = compute_phi(A, i, j)
        J = jacobi_matrix(A, i, j, phi)
        A = J.T @ A @ J
        iter_count += 1

    eigenvalues = np.diagonal(A)
    return eigenvalues, A

# Тестирование метода
A = np.array([[4, -2, 2],
              [-2, 2, -2],
              [2, -2, 3]])

eigenvalues, A_prime = jacobi_rotation(A)
print(eigenvalues, A_prime)
