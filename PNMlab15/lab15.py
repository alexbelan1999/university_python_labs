import func
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(-1.0, 2.5, 0.01)
y = np.tan(0.4 * x + 0.4) - x * x
ax.plot(x, y, 'k')
plt.title('График tg(0.4*x+0.4))=x^2')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

a = -1
b = 2.5
E = 0.001

func.table(a, b)
print()
func.dix(a, b, E)
print()
func.newton(a, b, E)
print()
func.secant(a, b, E)
print()
func.chord(a, b, E)
print()

a = 0.0
b = 1.0
func.table(a, b)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
x = np.arange(-1.0, 1.0, 0.01)
y = 5 * x ** 3 - x - 1
ax1.plot(x, y, 'k')
plt.title('График 5 * x**3 -x - 1 = 0')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
func.mpi(a, b, E)
