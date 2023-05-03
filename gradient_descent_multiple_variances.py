# Gradient Descnet 다변수 함수 일때
import numpy as np 
import sympy as sym # 문자에 대한 미분을 하기 위해 sympy import
from sympy.abc import x,y # x,y를 변수로 사용하기 위해 import x= x1, y=x2 라고 생각하면 된다.
import math #sqrt를 사용하기 위해 import 

def norm (a,b):  # L2 norm을 구한다. L2 norm은 우리가 아는 유클리드 거리(두 점사이의 거리)와 같음
    return math.sqrt((a**2+b**2)) # norm 값 리턴

def func(point): # 경사 하강법 대상이 되는 함수를 리턴하는 함수 
    x_val,y_val=point[0],point[1] # x좌표와 y좌표를 저장
    fun = sym.poly((1-x)**2+5*(y-x**2)**2) # 경사하강법을 사용할 함수를  정의한다.
    return fun.subs([(x, x_val),(y,y_val)]), fun # 첫번째 리턴값으로 함수에 x값과 y값을 대입한 값 (fun(x_val,y_val)), 두번째 리턴값으로 함수를 리턴한다.

def func_gradient(fun, val): # 함수의 그래디언트 값을 계산하고, 미분한 함수를 리턴하는 함수
    x_val,y_val=val[0],val[1] # x좌표와 y좌표를 저장
    _, function = fun(val) #함수식을 받아옴
    diff_x= sym.diff(function,x) #x에 대한 편미분
    diff_y= sym.diff(function,y) #y에 대한 편미분
    diff_x_val=diff_x.subs([(x, x_val),(y,y_val)]) # x에 대한 편미분 식에 (x,y) 값을 대입
    diff_y_val=diff_y.subs([(x, x_val),(y,y_val)]) # y에 대한 편미분 식에 (x,y) 값을 대입
    return norm(diff_x_val,diff_y_val), [diff_x,diff_y] # 미분값(norm값) , 미분식 반환
    # 편미분을 통해 미분값이 2개 나오므로, norm을 통해 미분값의 크기를 구함 (제곱해서 더하고 루트 씌움)

def gradient_descent(fun, init_point, lr_rate=1e-2, epsilon=1e-5): # 경사 하강법을 수행하는 함수
    cnt = 0 # 반복횟수를 저장하기 위한 cnt
    val = init_point #시작 위치(x,y)
    x_val,y_val=val # x좌표와 y좌표를 저장
    diff, _= func_gradient(fun, val) #시작위치에서의 첫 gradient
    while np.abs(diff) > epsilon: # 최소 점이라고 생각할 수 있는 epsilon보다 크다면 계속 반복문을 돌린다.
        diff_x_val= sym.diff(fun(val)[1],x).subs([(x, x_val),(y,y_val)]) # x에 대한 편미분 식에 (x,y) 값을 대입
        diff_y_val= sym.diff(fun(val)[1],y).subs([(x, x_val),(y,y_val)]) # y에 대한 편미분 식에 (x,y) 값을 대입
        x_val-=lr_rate*diff_x_val # 새로운 x값 = 기존 x값 - Learning rate * x의 편미분값 (diff_x_val)
        y_val-=lr_rate* diff_y_val # 새로운 y값 = 기존 y값 - Learning rate * y의 편미분값 (diff_y_val)
        val=[x_val,y_val] # val = [새로운 x값, 새로운 y값]
        diff, _ = func_gradient(fun, val) # 다시 gradient 값을 계산
        cnt += 1 # 수행한 횟수 count

        # 아래 print 문은 체크용으로 제출할때는 삭제하세요
        print(cnt,val[0],val[1]) # 연산횟수, x값, y값 

    print("함수: {}\n연산횟수: {}\n최소점: ({}, {}, {})".format(fun(val)[1], cnt, val[0], val[1], fun(val)[0]))

gradient_descent(fun=func,init_point=[-1.4,2])
