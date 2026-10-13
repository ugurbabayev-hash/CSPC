"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)

x_gd = 0.0
learning_rate = 0.1
max_iter = 1000
tolerance = 1e-7

for _ in range(max_iter):
    step = learning_rate * df(x_gd)
    x_gd -= step
    if abs(step) < tolerance:
        break

print(f"1) Gradient Descent : x = {x_gd:.4f}")
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)


x_newton = newton(df, x0=0.0, fprime=d2f)
print(f"2) Newton's Method  : x = {x_newton:.4f}")

#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")

res_slsqp = minimize(f, x0=0.0, method="SLSQP")
print(f"3) SLSQP Minimize   : x = {res_slsqp.x[0]:.4f}")

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?
def test_landscape(x0):
    x_gd = float(x0)
    lr = 0.01
    for _ in range(2000):
        step = lr * dg(x_gd)
        x_gd -= step
        if abs(step) < 1e-7:
            break
    print(f"1) Gradient Descent : x = {x_gd:.4f}, g(x) = {g(x_gd):.4f}")

    x_newt = newton(dg, x0=x0, fprime=d2g)
    curvature = d2g(x_newt)
    # d2g > 0 olarsa minimumdur, d2g < 0 olarsa maksimumdur
    point_type = "MINIMUM (d2g > 0)" if curvature > 0 else "MAKSIMUM (d2g < 0)"
    print(f"2) Newton's Method  : x = {x_newt:.4f}, d2g = {curvature:.4f} -> {point_type}")

    res_slsqp = minimize(g, x0=x0, method="SLSQP")
    print(f"3) SLSQP Minimize   : x = {res_slsqp.x[0]:.4f}, g(x) = {g(res_slsqp.x[0]):.4f}")

test_landscape(x0=0.0)
test_landscape(x0=2.0)
