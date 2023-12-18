import numpy as np

EPS = 1e-10

def integral_smoothing(vars, vals, m, x):
    """
    Вычисление функции сглаживания.
    """
    n = len(vars)
    A = np.zeros((m + 1, m + 1))
    b = np.zeros(m + 1)

    for i in range(m + 1):
        for j in range(m + 1):
            A[i, j] = sum(vars ** (i + j))

        b[i] = sum(vals * (vars ** i))

    coefs = np.linalg.solve(A, b)

    return sum(coefs[index] * (x ** index) for index in range(len(coefs)))


# Функция для тестирования
def test_integral_smoothing():
    # Тест 1: Простой случай
    vars_test1 = np.array([0, 1, 2], dtype=float)
    vals_test1 = np.array([1, 3, 5], dtype=float)
    expected_result1 = 3.0  # Ожидаемое значение при x = 1 и m = 1
    assert np.isclose(integral_smoothing(vars_test1, vals_test1, 1, 1), expected_result1), "Тест 1 провален"

    # Тест 2: Сложный случай
    vars_complex = np.array([1, 2, 3], dtype=float)
    vals_complex = np.array([1, 4, 9], dtype=float)  # y = x^2
    expected_complex = 6.25 
    assert np.isclose(integral_smoothing(vars_complex, vals_complex, 2, 2.5), expected_complex),  "Тест 2 провален"

    # Упрощенный тестовый случай
    # Используем линейное соотношение для проверки
    vars_simple = np.array([0, 1, 2, 3], dtype=float)
    vals_simple = np.array([2, 3, 5, 4], dtype=float)  # Пример линейных данных
    expected_simple = 3.5  # Ожидаемое значение при x = 1.5 и m = 1
    assert np.isclose(integral_smoothing(vars_simple, vals_simple, 1, 1.5), expected_simple), "Упрощенный тест 3 провален"

    # Более сложный тестовый случай
    # Используем квадратичное соотношение
    vars_complex = np.array([1, 2, 3, 4, 5], dtype=float)
    vals_complex = np.array([1, 4, 9, 16, 25], dtype=float)  # Квадратичная зависимость y = x^2
    expected_complex = 9.0  # Ожидаемое значение при x = 3 и m = 2
    assert np.isclose(integral_smoothing(vars_complex, vals_complex, 2, 3), expected_complex), "Сложный тест 4 провален"

    print("Все тесты успешно пройдены!")

# Тестовые данные
variables_lesson = np.array([0, 1, 2, 4], dtype=float)
values_lesson = np.array([0, 1, 4, 2], dtype=float)

variables_sw = np.array([0, 1, 2, 3], dtype=float)
values_sw = np.array([0, 2, 5, 3], dtype=float)

print("\nЗначение функции сглаживания на сетке для совместного решения при x = 1.5 и m = 1:", 
      round(integral_smoothing(variables_lesson, values_lesson, 1, 1.5), 3))
print("Значение функции сглаживания на сетке для самостоятельного решения при x = 1.5 и m = 1:", 
      round(integral_smoothing(variables_sw, values_sw, 1, 1.5), 3))

# Вызов функции тестирования
test_integral_smoothing()