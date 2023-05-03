# Gradient Descent 단변수 함수일때
import numpy as np
import sympy as sym
from sympy.abc import x

def func(val):
    fun = sym.poly(x**2 + 2*x + 3)
    return fun.subs(x, val), fun

def func_gradient(fun, val):
    _, function = fun(val) #함수식을 받아온다
    diff= sym.diff(function, x) #미분식 계산
    return diff.subs(x, val), diff #미분값, 미분식 반환

def gradient_descent(fun, init_point, lr_rate=1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point #시작 위치(x)
    diff, _= func_gradient(fun, val) #시작위치에서의 첫 gradient
    while np.abs(diff) > epsilon: # 최소 점이라고 생각할 수 있는 epsilon보다 큰 동안 계속 반복문을 돌린다.
        val -= lr_rate * diff # leaning_rate와 gradient(미분값)을 곱한 값을 빼주면서 update
        diff, _ = func_gradient(fun, val) # 다시 gradient 값을 계산
        cnt += 1 # 수행한 횟수 count

    print("함수: {}\n연산횟수: {}\n최소점: ({}, {})".format(fun(val)[1], cnt, val, fun(val)[0]))

gradient_descent(fun=func,init_point=3.0000)
