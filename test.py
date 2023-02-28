import sympy
from numpy import *
from sympy import symbols, Function, Eq, solve, pprint

y, u = symbols('y u', cls=Function)

x, t = sympy.symbols('x t')

A, B, C, D = sympy.symbols('A B C D')

# 임의로 u(x,t)를 u로 표현

u = Eq(A * (math.acos(B * x + C * t + D)) ** 2, 0)

p1 = Eq(diff(u, t) + u * diff(x,t) + diff(u, x, x, x), 0)

solve((p1, 0),(x,t,u))

print_solution = solve((p1, u), (A, B, C, D))

pprint(print_solution)

# print("A:%f B:%f C:% D:%f")
