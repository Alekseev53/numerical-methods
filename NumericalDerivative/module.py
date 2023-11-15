import numpy as np
import math

class NumericalDerivative:
    def __init__(self, h=1e-5):
        self.h = h

    def forward_difference(self, f, x):
        return (f(x + self.h) - f(x)) / self.h

    def backward_difference(self, f, x):
        return (f(x) - f(x - self.h)) / self.h

    def central_difference(self, f, x):
        """ Approximate the derivative of f at point x using central difference. """
        return (f(x + self.h) - f(x - self.h)) / (2 * self.h)

    def five_point_stencil(self, f, x):
        return (-f(x + 2*self.h) + 8*f(x + self.h) - 8*f(x - self.h) + f(x - 2*self.h)) / (12*self.h)

    def richardson_extrapolation(self, f, x):
        D1 = self.central_difference(f, x)
        D2 = self.central_difference(f, x + self.h/2)  # Use h/2 as the step size
        return D1 + (D1 - D2) / 3
