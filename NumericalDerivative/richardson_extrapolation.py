import math

class RichardsonExtrapolation:
    @staticmethod
    def select_stepsize(h, num_unknowns):
        if isinstance(h, list):
            if len(h) != num_unknowns:
                raise ValueError('Number of stepsizes ({}) not equal to number of unknowns ({})'.format(len(h), num_unknowns))
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
        f0 = func(h[0])
        f1 = func(h[1])

        h0h1n = (h[0] / h[1]) ** n
        f = (f0 - f1 * h0h1n) / (1 - h0h1n)
        c = (f0 - f) / (h[0] ** n)

        return {'f': f, 'n': n, 'c': c}

    @staticmethod
    def calculate_order_and_constant(func, f, h):
        f0 = func(h[0])
        f1 = func(h[1])

        n = math.log((f0 - f) / (f1 - f)) / math.log(h[0] / h[1])
        c = (f0 - f) / (h[0] ** n)

        return {'f': f, 'n': n, 'c': c}

    @staticmethod
    def richardson(func, h, knowns=None):
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
            raise NotImplementedError('Calculation of order, value, and error term constant not yet implemented.')
        elif num_unknowns == 2:
            if n is None:
                return RichardsonExtrapolation.calculate_order_and_constant(func, f, hset)
            elif f is None:
                return RichardsonExtrapolation.calculate_value_and_constant(func, n, hset)
        else:
            raise ValueError('Invalid set of knowns and unknowns.')
