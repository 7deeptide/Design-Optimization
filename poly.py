# Polynomial approximation (4-point cubic)
# -Erin Schmidt

import numpy as np

# make an array with random values between 0.05 and 0.15 with 4 enties
x = (0.05 + np.random.sample(4)*0.15).tolist()

# make an array of function values at at the 4 points of x
def f(x):
    return (1.11 + 1.11*x**(-0.18))/(1 - x)

f_array = []
i = 0
while i <= len(x) - 1:
    f_array.append(f(x[i]))
    i += 1

# use the equations from Vanderplaats 1984 to solve coefficients
q1 = x[2]**3 * (x[1] - x[0]) - x[2]**3 * (x[2] - x[0]) + x[0]**3 * (x[2] - x[1])
q2 = x[3]**3 * (x[1] - x[0]) - x[1]**3 * (x[3] -x[0]) + x[0]**3 * (x[3] - x[2])
q3 = (x[2] - x[1]) * (x[1] - x[0]) * (x[2] - x[0])
q4 = (x[3] - x[1]) * (x[1] - x[0]) * (x[3] - x[0])
q5 = f_array[2] * (x[1] - x[0]) - f_array[1] * (x[2] - x[0]) + f_array[0] * (x[2] - x[1])
q6 = f_array[3] * (x[1] - x[0]) - f_array[1] * (x[3] - x[0]) + f_array[0] * (x[3] - x[1])

a3 = (q3*q6 - q4*q5)/(q2*q3 - q1*q4)
a2 = (q5 - a3*q1)/q3
a1 = (f_array[1] - f_array[0])/(x[1] - x[0]) - a3*(x[1]**3 - x[0]**3)/(x[1] - x[0]) - a2*(x[0] + x[1])
a0 = f_array[0] - a1*x[0] - a2*x[0]**2 - a3*x[0]**3
a = [a0 ,a1, a2, a3]

# find the zeros of the polynomial
roots = np.roots(np.array(a))
print(roots)


