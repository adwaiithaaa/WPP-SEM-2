import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # roots at x = 1, 2, 3

a, b = 0.0, 4.0
tolerance = 1e-5
max_iter = 100
steps = []

for i in range(max_iter):
    c = (a + b) / 2
    steps.append(c)
    if abs(f(c)) < tolerance:
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

steps = np.array(steps)

x_vals = np.linspace(0, 4, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.plot(steps, f(steps), 'ro-', label='Bisection Steps')
plt.legend()
plt.title('Bisection Method Root Finding')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()