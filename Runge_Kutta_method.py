# Runge Kutta 방법

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

def Runge_Kutta_func(t): # Runge_Kutta 방법을 실행하는 함수
    start_t,end_t=1,2
    h=0.05
    y=-1
    i=start_t
    while True:
        if (t-i<h):
            df_1=get_y_prime(y,i)
            df_2=get_y_prime(y+h*df_1/2,i+h/2)
            df_3=get_y_prime(y+h*df_2/2,i+h/2)
            df_4=get_y_prime(y+h*df_3,i+h)
            next_y=y+(t-i)*(df_1+2*df_2+2*df_3+df_4)/6
            y=next_y
            break
        df_1=get_y_prime(y,i)
        df_2=get_y_prime(y+h*df_1/2,i+h/2)
        df_3=get_y_prime(y+h*df_2/2,i+h/2)
        df_4=get_y_prime(y+h*df_3,i+h)
        next_y=y+h*(df_1+2*df_2+2*df_3+df_4)/6
        y=next_y
        i+=h
        i=round(i,3)
    return y

def get_Runge_Kutta_values(): #1-2까지 0.001 단위로  Runge_Kutta값들을 리턴하는 함수
    values=[]
    start_t,end_t=1,2
    h=0.05
    y=-1
    i=start_t
    while i<=end_t:
        values.append(y)
        df_1=get_y_prime(y,i)
        df_2=get_y_prime(y+h*df_1/2,i+h/2)
        df_3=get_y_prime(y+h*df_2/2,i+h/2)
        df_4=get_y_prime(y+h*df_3,i+h)
        next_y=y+h*(df_1+2*df_2+2*df_3+df_4)/6
        y=next_y
        i+=h
        i=round(i,3)
    return values


t=np.arange(1.0,2.05,0.05)
exact_values=get_exact_values()
Runge_Kutta_values=get_Runge_Kutta_values()
print()
print("정확한 값")
print(exact_values)
print()
print("Runge Kutta 방법을 이용한 근사 값")
print(Runge_Kutta_values)
plt.plot(t, exact_values, 'r--',label="exact_value")
plt.plot(t,Runge_Kutta_values, 'b--',label="Runge_Kutta_values")
plt.xlabel('t')
plt.ylabel('Y')
plt.legend(loc='best', ncol=2)
plt.show()


