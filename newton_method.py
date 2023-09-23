import sympy as sp
from pprint import pprint

class Function:
    def __init__(self, function, is_polynomial=False):
        x = sp.symbols('x')
        self.is_polynomial = is_polynomial
        if is_polynomial:
            self.function = sum(c * x**i for i, c in enumerate(reversed(function)))  # создание полинома
        else:
            self.function = sp.sympify(function)  # преобразование строки в функцию
        self.derivative = sp.diff(self.function, x)  # вычисление производной

    def evaluate(self, x):
        return float(self.function.evalf(subs={sp.Symbol('x'): x}))  # оценка функции

    def derivative_eval(self, x):
        return float(self.derivative.evalf(subs={sp.Symbol('x'): x}))  # оценка производной

    # Метод Ньютона
    def newton_method(self, x0, epsilon):
        xn = x0
        while abs(self.evaluate(xn)) > epsilon:
            fxn = self.evaluate(xn)
            dfxn = self.derivative_eval(xn)
            if dfxn == 0:
                return f"Производная равна нулю при x = {xn}, метод не работает."
            xn = xn - fxn / dfxn
        return xn

    # Упрощенный метод Ньютона
    def simplified_newton_method(self, x0, epsilon):
        x1 = x0 - self.evaluate(x0) / self.derivative_eval(x0)
        xn = x1
        while abs(self.evaluate(xn)) > epsilon:
            fxn = self.evaluate(xn)
            dfx0 = self.derivative_eval(x0)
            if dfx0 == 0:
                return f"Производная равна нулю при x = {x0}, метод не работает."
            xn = xn - fxn / dfx0
        return xn

    # Метод Ньютона-Броуера
    def newton_brower_method(self, x0, epsilon, c):
        xn = x0
        while abs(self.evaluate(xn)) > epsilon:
            fxn = self.evaluate(xn)
            dfxn = self.derivative_eval(xn)
            if dfxn == 0:
                return f"Производная равна нулю при x = {xn}, метод не работает."
            xn = xn - c * fxn / dfxn
        return xn

    # Метод секущих
    def secant_method(self, x0, epsilon, delta):
        fx0 = self.evaluate(x0)
        dfx0 = (self.evaluate(x0) - self.evaluate(x0 - delta)) / delta
        if dfx0 == 0:
            return f"Производная равна нулю при x = {x0}, метод не работает."
        x1 = x0 - fx0 / dfx0
        xn = x1
        while abs(self.evaluate(xn)) > epsilon:
            dfxn = (self.evaluate(xn) - self.evaluate(xn - 1)) / (xn - (xn - 1))
            if dfxn == 0:
                return f"Производная равна нулю при x = {xn}, метод не работает."
            xn = xn - self.evaluate(xn) / dfxn
        return xn

    # Метод хорд
    def chord_method(self, a, b, epsilon):
        if self.evaluate(a) > 0:
            x0 = b
        else:
            x0 = a
        xn = x0
        while abs(self.evaluate(xn)) > epsilon:
            if self.evaluate(a) > 0:
                denominator = (self.evaluate(xn) - self.evaluate(a))
                if denominator == 0:
                    return f"Деление на ноль при x = {xn}, метод не работает."
                xn = a - (self.evaluate(a) * (xn - a)) / denominator
            else:
                denominator = (self.evaluate(b) - self.evaluate(xn))
                if denominator == 0:
                    return f"Деление на ноль при x = {xn}, метод не работает."
                xn = xn - (self.evaluate(xn) * (b - xn)) / denominator
        return xn

# Тестирование каждого метода индивидуально для полиномиальных и неполиномиальных функций
test_results = {}

# Полиномиальная функция
poly_func = Function([1, -6, 11, -6], is_polynomial=True)
test_results['polynomial'] = {}
test_results['polynomial']['newton_method'] = poly_func.newton_method(3, 1e-6)
test_results['polynomial']['simplified_newton_method'] = poly_func.simplified_newton_method(3, 1e-6)
test_results['polynomial']['newton_brower_method'] = poly_func.newton_brower_method(3, 1e-6, 1)
test_results['polynomial']['secant_method'] = poly_func.secant_method(3, 1e-6, 0.01)
test_results['polynomial']['chord_method'] = poly_func.chord_method(2, 3, 1e-6)

# Неполиномиальная функция
non_poly_func = Function("sin(x)/x + exp(x) - 1")
test_results['non_polynomial'] = {}
test_results['non_polynomial']['newton_method'] = non_poly_func.newton_method(0.5, 1e-6)
test_results['non_polynomial']['simplified_newton_method'] = non_poly_func.simplified_newton_method(0.5, 1e-6)
test_results['non_polynomial']['newton_brower_method'] = non_poly_func.newton_brower_method(0.5, 1e-6, 1)
test_results['non_polynomial']['secant_method'] = non_poly_func.secant_method(0.5, 1e-6, 0.01)
test_results['non_polynomial']['chord_method'] = non_poly_func.chord_method(0.1, 1, 1e-6)

pprint(test_results)
