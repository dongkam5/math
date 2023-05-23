# Adams - Bashforth method
# Adams - Moulton method
import math
import numpy as np
import matplotlib.pyplot as plt

def get_y_prime(y,x): # y' 값을 리턴해주는 함수
    return (y-x**2) 

def exact_func (x): # 값을 비교할 실제 함수
    return (2+2*x+x**2-math.exp(x))

def get_exact_values(): #1-2까지 0.001 단위로 실제 값들을 리턴하는 함수
    start_x,end_x=0,3.3
    h=0.1
    values=[]
    i=start_x
    while i<=end_x:
        values.append(2+2*i+i**2-math.exp(i)) 
        i+=h
        i=round(i,2)
    return values

def Runge_Kutta_func(x): # Runge_Kutta 방법을 실행하는 함수
    start_x,end_x=0,3.3
    h=0.1
    y=1
    i=start_x
    while True:
        if (x-i<h):
            df_1=get_y_prime(y,i)
            df_2=get_y_prime(y+h*df_1/2,i+h/2)
            df_3=get_y_prime(y+h*df_2/2,i+h/2)
            df_4=get_y_prime(y+h*df_3,i+h)
            next_y=y+(x-i)*(df_1+2*df_2+2*df_3+df_4)/6
            y=next_y
            break
        df_1=get_y_prime(y,i)
        df_2=get_y_prime(y+h*df_1/2,i+h/2)
        df_3=get_y_prime(y+h*df_2/2,i+h/2)
        df_4=get_y_prime(y+h*df_3,i+h)
        next_y=y+h*(df_1+2*df_2+2*df_3+df_4)/6
        y=next_y
        i+=h
        i=round(i,2)
    return y

def get_Runge_Kutta_values(): #1-2까지 0.001 단위로  Runge_Kutta값들을 리턴하는 함수
    values=[]
    start_x,end_x=0,3.3
    h=0.1
    y=1
    i=start_x
    while i<=end_x:
        values.append(y)
        df_1=get_y_prime(y,i)
        df_2=get_y_prime(y+h*df_1/2,i+h/2)
        df_3=get_y_prime(y+h*df_2/2,i+h/2)
        df_4=get_y_prime(y+h*df_3,i+h)
        next_y=y+h*(df_1+2*df_2+2*df_3+df_4)/6
        y=next_y
        i+=h
        i=round(i,2)
    return values

def get_Adams_Bashforth_method (): #아담스 베시포드 메소드 구현 함수
    Runge_Kutta_values=get_Runge_Kutta_values()
    y0=Runge_Kutta_values[0] # 현재 전전전 단계 값
    y1=Runge_Kutta_values[1] # 현재 전전 단계 값
    y2=Runge_Kutta_values[2] # 현재 전 단계 값
    y3=Runge_Kutta_values[3] #현재 값
    values=[y0,y1,y2]
    start_x,end_x=0,3.3
    h=0.1
    i=start_x+3*h
    while i<=end_x:
        values.append(y3)
        next_y=y3+h*(55*get_y_prime(y3,i)-59*get_y_prime(y2,i-h)+37*get_y_prime(y1,i-2*h)-9*get_y_prime(y0,i-3*h))/24
        y0=y1
        y1=y2
        y2=y3
        y3=next_y
        i+=h
        i=round(i,2)
    return values

def get_Adams_Moulton_method (): # 암담스 몰턴 메소드 구현 함수 
    Runge_Kutta_values=get_Runge_Kutta_values()
    Adams_Bashforth_values=get_Adams_Bashforth_method()
    idx=3
    y0=Runge_Kutta_values[0] # 현재 전전 단계 값
    y1=Runge_Kutta_values[1] # 현재 전 단계 값
    y2=Runge_Kutta_values[2] # 현재 단계 값
    values=[y0,y1,y2]
    start_x,end_x=0,3.3
    h=0.1
    i=start_x+2*h
    while i<end_x:
        next_y=Adams_Bashforth_values[idx]
        next_y=y2+h*(9*get_y_prime(next_y,i+h)+19*get_y_prime(y2,i)-5*get_y_prime(y1,i-h)+get_y_prime(y0,i-2*h))/24
        y0=y1
        y1=y2
        y2=next_y
        values.append(next_y)
        i+=h
        idx+=1
        i=round(i,2)
    return values

x=np.arange(0.0,3.4,0.1)
exact_values=get_exact_values()
Runge_Kutta_values=get_Runge_Kutta_values()
Adams_Bashforth=get_Adams_Bashforth_method()
Adams_Moulton_method=get_Adams_Moulton_method()
print()
print("정확한 값")
print(exact_values)
print()
print("Runge Kutta 방법을 이용한 근사 값")
print(Runge_Kutta_values)
print()
print("Adams_Bashforth 방법을 이용한 근사 값")
print(Adams_Bashforth)
print()
print("Adams_Moulton_method 방법을 이용한 근사 값")
print(Adams_Moulton_method)
print()
plt.plot(x, exact_values, 'r--',label="exact_value")
plt.plot(x,Runge_Kutta_values, 'b--',label="Runge_Kutta_values")
plt.plot(x,Adams_Bashforth,'g--',label="Adams_Bashforth_values")
plt.plot(x,Adams_Moulton_method,'c--',label="Adams_Moulton_values")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()
