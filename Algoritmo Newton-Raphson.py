# coding=utf-8
from sympy import *
__author__ = 'David Cardozo'
x = symbols('x')


def metodonewton():
    str_expr = raw_input('Introduzca una función en la variable x: ')
    x0 = input('Introduzca un valor cercano de una de las raices: ')
    itermax = input('Introduzca un valor de maximas iteraciones: ')
    tol = input('Introduzca un porcentaje de tolerancia: ')
    expr = sympify(str_expr)
    diffexpr = diff(expr, x)
    contador = 0
    xraiz = 0
    flag = True
    while flag:
        x_rviejo = x0
        x_rnuevo = x_rviejo - ((expr.evalf(subs={x: x_rviejo}))/diffexpr.evalf(subs={x: x_rviejo}))
        if contador > itermax:
            flag = False
        if contador != 0:
            ea = abs((x_rnuevo - x_rviejo) / x_rnuevo) * 100
            if ea < tol:
                flag = False
        print x_rnuevo
        contador += 1
        x0 = x_rnuevo
    return xraiz

metodonewton()
