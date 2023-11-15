import unittest
import math
from module import NumericalDerivative  

class TestNumericalDerivative(unittest.TestCase):

    def setUp(self):
        self.h = 1e-6
        self.derivative_calculator = NumericalDerivative(h=self.h)

    def test_forward_difference(self):
        x = math.pi / 4
        expected = math.cos(x)
        result = self.derivative_calculator.forward_difference(math.sin, x)
        self.assertAlmostEqual(result, expected, delta=self.h)

    def test_backward_difference(self):
        x = math.pi / 4
        expected = math.cos(x)
        result = self.derivative_calculator.backward_difference(math.sin, x)
        self.assertAlmostEqual(result, expected, delta=self.h)

    def test_central_difference(self):
        x = math.pi / 4
        expected = math.cos(x)
        result = self.derivative_calculator.central_difference(math.sin, x)
        self.assertAlmostEqual(result, expected, delta=self.h)

    def test_five_point_stencil(self):
        x = math.pi / 4
        expected = math.cos(x)
        result = self.derivative_calculator.five_point_stencil(math.sin, x)
        self.assertAlmostEqual(result, expected, delta=self.h)

    def test_richardson_extrapolation(self):
        x = 1
        expected = math.exp(x)
        result = self.derivative_calculator.richardson_extrapolation(math.exp, x)
        self.assertAlmostEqual(result, expected, delta=self.h)

if __name__ == '__main__':
    unittest.main()
