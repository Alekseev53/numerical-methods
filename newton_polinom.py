# Полная программа для визуализации интерполяционного полинома Ньютона
# с использованием равноотстоящих узлов и узлов Чебышева

import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
x_values = np.array([0, 1, 2, 3])
f_values = np.array([1, 2, 4, 1])

# Функции для вычисления разделенных разностей и полинома Ньютона
def divided_differences(x, f):
    n = len(f)
    coef = np.zeros([n, n])
    coef[:,0] = f
    
    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
    return coef

def newton_polynomial(x, coef, x_point):
    n = len(x) - 1
    p = coef[n]
    for k in range(1, n+1):
        p = coef[n-k] + (x_point - x[n-k])*p
    return p

# Расчет разделенных разностей для исходного набора значений
coef = divided_differences(x_values, f_values)

# Функция для генерации узлов Чебышева
def chebyshev_nodes(n, a, b):
    return 0.5*(a+b) + 0.5*(b-a)*np.cos((2*np.arange(1, n+1)-1)/(2*n)*np.pi)

# Генерация узлов Чебышева для интервала [0, 3]
n = len(x_values)  # количество узлов
a, b = x_values[0], x_values[-1]  # начало и конец интервала
chebyshev_x_values = chebyshev_nodes(n, a, b)

# Значения функции f в узлах Чебышева, интерполяция через исходные значения f_values
chebyshev_f_values = np.interp(chebyshev_x_values, x_values, f_values)

# Расчет разделенных разностей для узлов Чебышева
chebyshev_coefs = divided_differences(chebyshev_x_values, chebyshev_f_values)

# Вычисление значений полиномов на более плотной сетке
x_dense = np.linspace(min(x_values), max(x_values), 100)
newton_y_dense = [newton_polynomial(x_values, coef[0, :], x_point) for x_point in x_dense]
chebyshev_y_dense = [newton_polynomial(chebyshev_x_values, chebyshev_coefs[0, :], x_point) for x_point in x_dense]

# Вычисление интерполяционного полинома Ньютона для равноотстоящих узлов в точке x* = 1.5
N3_uneven = newton_polynomial(x_values, coef[0, :], 1.5)

# Вычисление интерполяционного полинома Ньютона для узлов Чебышева в точке x* = 1.5
N3_chebyshev = newton_polynomial(chebyshev_x_values, chebyshev_coefs[0, :], 1.5)

# Выведем значения полиномов и коэффициентов
print("Значение интерполяционного полинома Ньютона для равноотстоящих узлов в точке x* = 1.5:", N3_uneven)
print("Значение интерполяционного полинома Ньютона для узлов Чебышева в точке x* = 1.5:", N3_chebyshev)
print("Коэффициенты интерполяционного полинома Ньютона для равноотстоящих узлов:", coef[0, :])
print("Коэффициенты интерполяционного полинома Ньютона для узлов Чебышева:", chebyshev_coefs[0, :])

# Визуализация результатов
plt.figure(figsize=(14, 7))

# Полином для равноотстоящих узлов
plt.subplot(1, 2, 1)
plt.plot(x_dense, newton_y_dense, label='Newton Polynomial - Evenly Spaced Nodes')
plt.plot(x_values, f_values, 'ro', label='Data Points - Evenly Spaced Nodes')
plt.title('Newton Polynomial - Evenly Spaced Nodes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Полином для узлов Чебышева
plt.subplot(1, 2, 2)
plt.plot(x_dense, chebyshev_y_dense, label='Newton Polynomial - Chebyshev Nodes')
plt.plot(chebyshev_x_values, chebyshev_f_values, 'bo', label='Data Points - Chebyshev Nodes')
plt.title('Newton Polynomial - Chebyshev Nodes')
plt.xlabel('x')
plt.legend()

plt.tight_layout()
plt.show()