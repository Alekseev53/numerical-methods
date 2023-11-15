import math

class RichardsonExtrapolation:
    @staticmethod
    def select_stepsize(h, num_unknowns):
        """
        Выбор шагов для экстраполяции Ричардсона.

        Если 'h' является списком, то функция возвращает этот список.
        Если 'h' не является списком, то функция создает список шагов, начиная с 'h'
        и делит 'h' на 2 на каждом следующем шаге, пока не достигнет нужного количества шагов.

        Параметры:
        h: начальный шаг или список шагов
        num_unknowns: количество неизвестных, для которых нужно определить шаги

        Возвращает список шагов.
        """
        if isinstance(h, list):
            if len(h) != num_unknowns:
                raise ValueError('Количество шагов ({}) не соответствует количеству неизвестных ({})'.format(len(h), num_unknowns))
            else:
                return h
        else:
            h0 = h
            stepsizes = [h0]
            for i in range(1, num_unknowns):
                h0 /= 2
                stepsizes.append(h0)
            return stepsizes

    @staticmethod
    def calculate_value_and_constant(func, n, h):
        """
        Рассчитывает значение функции и постоянную для заданного порядка n.

        Параметры:
        func: функция, для которой выполняется экстраполяция
        n: порядок точности
        h: список шагов

        Возвращает словарь с расчитанными значениями f, n и постоянной c.
        """
        f0 = func(h[0])
        f1 = func(h[1])

        h0h1n = (h[0] / h[1]) ** n
        f = (f0 - f1 * h0h1n) / (1 - h0h1n)
        c = (f0 - f) / (h[0] ** n)

        return {'f': f, 'n': n, 'c': c}

    @staticmethod
    def calculate_order_and_constant(func, f, h):
        """
        Рассчитывает порядок и постоянную для заданного значения функции.

        Параметры:
        func: функция, для которой выполняется экстраполяция
        f: известное значение функции
        h: список шагов

        Возвращает словарь с расчитанным порядком n и постоянной c.
        """
        f0 = func(h[0])
        f1 = func(h[1])

        n = math.log((f0 - f) / (f1 - f)) / math.log(h[0] / h[1])
        c = (f0 - f) / (h[0] ** n)

        return {'f': f, 'n': n, 'c': c}

    @staticmethod
    def richardson(func, h, knowns=None):
        """
        Основная функция для выполнения экстраполяции Ричардсона.

        Определяет необходимые параметры и вызывает соответствующие функции для расчета.
        В зависимости от известных значений (knowns) выполняет различные расчеты.

        Параметры:
        func: функция, для которой выполняется экстраполяция
        h: начальный шаг или список шагов
        knowns: словарь с известными значениями (может содержать 'n', 'f')

        Возвращает результаты расчетов в зависимости от заданных параметров.
        """
        if knowns is None:
            knowns = {}
        n = knowns.get('n')
        f = knowns.get('f')
        num_unknowns = 1

        if n is None:
            num_unknowns += 1
        if f is None:
            num_unknowns += 1

        hset = RichardsonExtrapolation.select_stepsize(h, num_unknowns)

        if num_unknowns == 3:
            raise NotImplementedError('Расчет порядка, значения и постоянной погрешности пока не реализован.')
        elif num_unknowns == 2:
            if n is None:
                return RichardsonExtrapolation.calculate_order_and_constant(func, f, hset)
            elif f is None:
                return RichardsonExtrapolation.calculate_value_and_constant(func, n, hset)
        else:
            raise ValueError('Неверный набор известных и неизвестных значений.')

    @staticmethod
    def improve_approximation(func, h, t, k0, max_iter=200, tolerance=1e-11):
        """
        Улучшает приближение, используя процесс экстраполяции Ричардсона.

        Параметры:
        func: функция для экстраполяции.
        h: начальный шаг.
        t: константа для изменения шага.
        k0: начальный порядок ошибки.
        max_iter: максимальное количество итераций.
        tolerance: желаемая точность приближения.

        Возвращает улучшенное приближение.
        """
        current_h = h
        for i in range(max_iter):
            A0 = func(current_h)
            A1 = func(current_h / t)
            improved_approximation = (t**k0 * A1 - A0) / (t**k0 - 1)

            if abs(improved_approximation - A0) < tolerance:
                return improved_approximation

            current_h /= 2  # Полагаем новое значение шага

        raise ValueError("Не удалось достичь желаемой точности за указанное количество итераций.")
