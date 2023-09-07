def sqrt_a(a, tol=1e-10, max_iter=1000):
    xn = a / 2  # Начальное приближение
    for _ in range(max_iter):
        xn1 = 0.5 * (a / xn + xn)
        if abs(xn1 - xn) < tol:
            return xn1
        xn = xn1
    else:
        print("MAX кол-во итераций превышено")
        return None

a = 5
result = sqrt_a(a)
if result is not None:
    print(f"sqrt{a} = {result}")
