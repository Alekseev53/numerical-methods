# Данные точки
x = [3, 4, 5, 6]
f_x = [1, 0, 4, 2]
x_star = 4.5

# 1. Глобальный метод с использованием полиномов Лагранжа
def lagrange_interpolation(x, f_x, x_star):
    """
    Вычисляет интерполированное значение с использованием полиномов Лагранжа для заданного x_star.
    """
    n = len(x)
    P_x_star = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x_star - x[j]) / (x[i] - x[j])
        P_x_star += f_x[i] * L_i
    return P_x_star

# 2. Линейная интерполяция
def linear_interpolation(x1, x2, f_x1, f_x2, x_star):
    """
    Вычисляет интерполированное значение с использованием линейной интерполяции между x1 и x2 для заданного x_star.
    """
    return ((x_star - x2) * f_x1 + (x1 - x_star) * f_x2) / (x1 - x2)

# 3. Параболическая интерполяция
def parabolic_interpolation(x_values, f_x_values, x_star):
    """
    Вычисляет интерполированное значение с использованием параболической интерполяции для заданного x_star.
    """
    x0, x1, x2 = x_values
    f_x0, f_x1, f_x2 = f_x_values

    b0 = f_x0
    b1 = (f_x1 - f_x0) / (x1 - x0)
    b2 = ((f_x2 - f_x1) / (x2 - x1) - b1) / (x2 - x0)

    return b0 + b1 * (x_star - x0) + b2 * (x_star - x0) * (x_star - x1)

# Оцените интерполяцию на x_star с использованием трех методов
global_result = lagrange_interpolation(x, f_x, x_star)
linear_result = linear_interpolation(x[1], x[2], f_x[1], f_x[2], x_star)
parabola_1_result = parabolic_interpolation(x[:3], f_x[:3], x_star)
parabola_2_result = parabolic_interpolation(x[1:], f_x[1:], x_star)
parabolic_result = (parabola_1_result + parabola_2_result) / 2

# Вывод результатов
print(f"Глобальный метод (полиномы Лагранжа): f(x*) = {global_result}")
print(f"Линейная интерполяция: f(x*) = {linear_result}")
print(f"Параболическая интерполяция (усредненная): f(x*) = {parabolic_result}")
