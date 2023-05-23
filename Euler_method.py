# 오일러 방법

import numpy as np
import matplotlib.pyplot as plt

def get_y_prime(y,t): # y' 값을 리턴해주는 함수
    return (1/t**2-y/t-y**2) 

def exact_func (t): # 값을 비교할 실제 함수
    return (-1/t)

def get_exact_values(): #1-2까지 0.001 단위로 실제 값들을 리턴하는 함수
    start_t,end_t=1,2
    h=0.05
    values=[]
    i=start_t
    while i<=end_t:
        values.append((-1/i))
        i+=h
        i=round(i,3)
    return values

def euler_method_func(t): # 오일러 방법을 실행하는 함수
    start_t,end_t=1,2
    h=0.05
    y=-1
    i=start_t
    while True:
        if (t-i<h):
            df=get_y_prime(y,i)
            next_y=y+(t-i)*df
            y=next_y
            break
        df=get_y_prime(y,i)
        next_y=y+h*df
        y=next_y
        i+=h
        i=round(i,3)
    return y

def get_euler_method_values(): #1-2까지 0.001 단위로 오일러 방법 값들을 리턴하는 함수
    values=[]
    start_t,end_t=1,2
    h=0.05
    y=-1
    i=start_t
    while i<=end_t:
        values.append(y)
        df=get_y_prime(y,i)
        next_y=y+h*df
        y=next_y
        i+=h
        i=round(i,3)
    return values


t=np.arange(1.0,2.05,0.05)
exact_values=get_exact_values()
euler_method_values=get_euler_method_values()
print()
print("정확한 값")
print(exact_values)
print()
print("오일러 방법을 이용한 근사 값")
print(euler_method_values)
plt.plot(t, exact_values, 'r--',label="exact_value")
plt.plot(t,euler_method_values, 'b--',label="euler_method_value")
plt.xlabel('t')
plt.ylabel('Y')
plt.legend(loc='best', ncol=2)
plt.show()


