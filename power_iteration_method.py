import numpy as np

def power_iteration(A, num_iterations=100, tol=1e-6):
    """
    Выполняет метод степенной итерации для матрицы A.
    
    Параметры:
    - A: матрица n x n
    - num_iterations: максимальное количество итераций
    - tol: критерий остановки
    
    Возвращает:
    - lambda_1: доминирующее собственное значение
    - b_k: соответствующий собственный вектор
    """
    
    n = A.shape[0]
    b_k = np.random.rand(n)  # Инициализируем случайный вектор
    b_k = b_k / np.linalg.norm(b_k)
    
    for _ in range(num_iterations):
        # Умножаем вектор на матрицу
        w = np.dot(A, b_k)
        # Нормализация вектора
        b_next = w / np.linalg.norm(w)
        
        # Проверка на сходимость
        if np.linalg.norm(b_next - b_k) < tol:
            break
        
        b_k = b_next
    
    # Вычисляем соответствующее собственное значение
    lambda_1 = np.dot(b_k.T, np.dot(A, b_k))
    
    return lambda_1, b_k

# Тестирование
def test():
    A = np.array([[4, 2], [2, 3]])
    lambda_1, b_k = power_iteration(A)
    print("Доминирующее собственное значение:", lambda_1)
    print("Соответствующий собственный вектор:", b_k)

    # Проверка с помощью numpy
    eigenvalues, eigenvectors = np.linalg.eig(A)
    max_index = np.argmax(np.abs(eigenvalues))
    print("Ожидаемое собственное значение:", eigenvalues[max_index])
    print("Ожидаемый собственный вектор:", eigenvectors[:, max_index])

test()
