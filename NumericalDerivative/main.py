import math
from module import NumericalDerivative

# Example usage
def sin_function(x):
    return math.sin(x)

def exp_function(x):
    return math.exp(x)

derivative_calculator = NumericalDerivative(h=1e-6)

# Calculating derivatives of sine function
x = math.pi / 4
forward_diff = derivative_calculator.forward_difference(sin_function, x)
backward_diff = derivative_calculator.backward_difference(sin_function, x)
central_diff = derivative_calculator.central_difference(sin_function, x)
five_point_diff = derivative_calculator.five_point_stencil(sin_function, x)

print("Forward Difference:", forward_diff)
print("Backward Difference:", backward_diff)
print("Central Difference:", central_diff)
print("Five Point Stencil:", five_point_diff)

# Using Richardson Extrapolation
x = 1
richardson_result = derivative_calculator.richardson_extrapolation(exp_function, x)
print("Richardson Extrapolation:", richardson_result)
